#  gitabel
#  the world's smallest project management tool
#  reports relabelling times in github (time in seconds since epoch)
#  thanks to dr parnin
#  todo:
#    - ensure events sorted by time
#    - add issue id
#    - add person handle

"""
You will need to add your authorization token in the code.
Here is how you do it.

1) In terminal run the following command

curl -i -u <your_username> -d '{"scopes": ["repo", "user"], "note": "OpenSciences"}' https://api.github.com/authorizations

2) Enter ur password on prompt. You will get a JSON response. 
In that response there will be a key called "token" . 
Copy the value for that key and paste it on line marked "token" in the attached source code. 

3) Run the python file. 

     python gitable.py

"""
 
from __future__ import print_function
import urllib2
import json
import re,datetime
import sys

name_i = 65
users = {}

class L():
  "Anonymous container"
  def __init__(i,**fields) : 
    i.override(fields)
  def override(i,d): i.__dict__.update(d); return i
  def __repr__(i):
    d = i.__dict__
    name = i.__class__.__name__
    return name+'{'+' '.join([':%s %s' % (k,pretty(d[k])) 
                     for k in i.show()])+ '}'
  def show(i):
    lst = [str(k)+" : "+str(v) for k,v in i.__dict__.iteritems() if v != None]
    return ',\t'.join(map(str,lst))

  
def secs(d0):
  if not d0:
    return 0
  d     = datetime.datetime(*map(int, re.split('[^\d]', d0)[:-1]))
  epoch = datetime.datetime.utcfromtimestamp(0)
  delta = d - epoch
  return delta.total_seconds()
 
def dump1(u,issues):
  global name_i
  token = "token" # <===
  request = urllib2.Request(u, headers={"Authorization" : "token "+token})
  v = urllib2.urlopen(request).read()
  w = json.loads(v)
  print ("************************************")
  fi = open("raw_data.txt","a+")
  fi.write(str(w))
  fi.close()
  print ("************************************")
  if not w: return False
  for event in w:
    issue_id = event['issue']['number']
    if not event.get('label'): continue
    created_at = secs(event['created_at'])
    i_created_at = secs(event['issue']['created_at'])
    closed_at = 0
    if event['issue']['closed_at'] != None:
        closed_at = secs(event['issue']['closed_at'])
        i_open_total = closed_at - i_created_at
    else: 
        i_open_total = -1
    comments = event['issue']['comments']
    action = event['event']
    label_name = event['label']['name']
    ###anonymize the name
    user = event['actor']['login']
    if user not in users.keys():
      users[user] = chr(name_i)
      name_i+=1
    user = users[user]
    milestone = event['issue']['milestone']
        ##add stuff we need
    try:
      updtd = secs(event['issue']['updated_at'])
    except:
      print("screw u")
      updtd = "None"
    milestone_closed = "None"
    milestone_due = "None"
    milestone_created = "None"
    milestone_total = 0
    if milestone != None :
        milestone = milestone['title']
        milestone_created = secs(event['issue']['milestone']['created_at'])
        milestone_due = secs(event['issue']['milestone']['due_on'])
        milestone_closed = secs(event['issue']['milestone']['closed_at'])
        milestone_open_issues = event['issue']['milestone']['open_issues']
        milestone_closed_issues = event['issue']['milestone']['closed_issues']
        milestone_total = milestone_open_issues + milestone_closed_issues
    eventObj = L(when=created_at,
                 opened=i_created_at,
                 ended=closed_at,
                 alive=i_open_total,
                 action = action,
                 comments=comments,
                 what = label_name,
                 user = user,
                 milestone_name = milestone,
                 updated = updtd,
                 milestone_created = milestone_created,
                 milestone_due = milestone_due,
                 milestone_closed = milestone_closed,
                 milestone_total = milestone_total
                 ) ##put new objects in eventObj
    all_events = issues.get(issue_id)
    if not all_events: all_events = []
    all_events.append(eventObj)
    issues[issue_id] = all_events
  return True

def dump(u,issues):
  try:
    return dump1(u, issues)
  except Exception as e: 
    print(e)
    print("Contact TA")
    return False

def launchDump():
  page = 1
  file = open("Data_Output3.txt", "w")
  issues = dict()
  while(True):
##    doNext = dump('https://api.github.com/repos/opensciences/opensciences.github.io/issues/events?page=' + str(page), issues)
##    doNext = dump('https://api.github.com/repos/incognito666/tarantula-python/issues/events?page=' + str(page), issues)
##    doNext = dump('https://api.github.com/repos/SuperCh-SE-NCSU/ProjectScraping/issues/events?page=' + str(page), issues)
    doNext = dump('https://api.github.com/repos/CSC510-2015-Axitron/maze/issues/events?page=' + str(page), issues)
    file.write("page "+ str(page)+'\n')
    page += 1
    if not doNext : break
  for issue, events in issues.iteritems():
    file.write("ISSUE " + str(issue)+'\n')
    for event in events:
        file.write(event.show()+'\n')
        ## print to file after adding params
    file.write('\n')
  file.close() 
    
launchDump()


  
   
 
