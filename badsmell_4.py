import urllib2
import json

def findFeature():
  ##1. all labels are used
  #fetch labels
  label_url = "https://api.github.com/repos/incognito666/tarantula-python/labels"
  token = "5384e37c678695b0325a97bb5c003bd4ff73f607" # <===
  request = urllib2.Request(label_url, headers={"Authorization" : "token "+token})
  res = urllib2.urlopen(request).read()
  labels = []
  r = json.loads(res)
  for l in range(0,len(r)):
    labels.append(str(r[l]['name']))
    
  #f = open("Data_Output.txt", "r")
  f=open("Data_Output.txt","r")
  assigned=[]
  unassigned=[]
  line = f.readline()
  while line:
      #print(line)
##      print("---------------")
      if "ISSUE" in line:
	  issue=line[6:-1]
	  #print issue
      target = line.find("user")
      if target != -1:
          start = line.find(":",target)
          end = line.find(",",start)
          substr = line[start+2:end]
	  #print len(substr)
	  #print substr
	  if not substr:		
		issue.split("\n")
		#print issue
		unassigned.append(issue)
      line = f.readline()
  if len(unassigned)!=0:
	print "The following are the unassigned Issues:\n"
	print unassigned
	print "Badsmell detected"
  else:
	print "All Issues have been assigned"
  f.close()
  
findFeature()
