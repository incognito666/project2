import urllib2
import json

def findFeature():
  ##1. all labels are used
  labels = ["Design","Code","Unit Test", "Integration Test",
            "Code Review", "Recover", "bug", "duplicate", "enhancement",
            "help wanted", "invalid", "question", "wontfix"]
  #fetch labels
  #label_url = "https://api.github.com/repos/incognito666/tarantula-python/labels"
  #token = "5384e37c678695b0325a97bb5c003bd4ff73f607" # <===
  #request = urllib2.Request(label_url, headers={"Authorization" : "token "+token})
  #res = urllib2.urlopen(request).read()
  #labels = []
  #r = json.loads(res)
  #for l in range(0,len(r)):
   # labels.append(str(r[l]['name']))
    
  #f = open("Data_Output.txt", "r")
  f=open("Data_Output.txt","r")
  really_bad=[]
  comments=[]
  line = f.readline()
  while line:
      #print(line)
##      print("---------------")
      if "ISSUE" in line:
	  issue=line[6:-1]
	  #print issue
      target = line.find("comments")
      target1=line.find("what")
      if target != -1:
          start = line.find(":",target)
          end = line.find(",",start)
          substr = line[start+2:end]
	  #print len(substr)
	  #print substr
	  if substr=='0':		
		issue.split("\n")
		#print issue
		comments.append(issue)
      if target1 != -1:
          start1 = line.find(":",target1)
          end1 = line.find(",",start1)
          substr1 = line[start1+2:end1]
          #print len(substr)
          #print substr1
          if  substr1=="question":               
                issue.split("\n")
                really_bad.append(issue)
 	

      line = f.readline()
  if len(comments)!=0:
	print "The following are issues with lack of communication:\n"
	print comments
	print "Badsmell detected"

  if len(really_bad)!=0:
        print "The following are issues with really bad communication:\n"
        print really_bad
        print "Really bad Badsmell detected"
  else:
        print "All Issues have been well communicated"

  f.close()
  
findFeature()
