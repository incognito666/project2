import urllib2
import json

def findFeature():
  ##1. all labels are used
  labels = ["Design","Code","Unit Test", "Integration Test",
            "Code Review", "Recover", "bug", "duplicate", "enhancement",
            "help wanted", "invalid", "question", "wontfix"]
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
  single_issue=[]
  count=0
  issue=0
  line = f.readline()
  while line:
      #print(line)
##      print("---------------")
      if "ISSUE" in line:
	  if(count==1):
		single_issue.append(issue)
		
	  issue=line[6:-1]
	  
	  count=0
	  #print issue
      target = line.find("milestone_closed")
      if not target:
	  count=count+1	
      line = f.readline()



  if len(single_issue)!=0:
	print "The following are the single Issues:\n"
	print single_issue
	print "Badsmell detected"
  else:
	print "All Issues have more than one milestone"
  f.close()
  
findFeature()
