import urllib2
import json

def findFeature():
  ##1. all labels are used
  labels = ["Design","Code","Unit Test", "Integration Test",
            "Code Review", "Recover", "bug", "duplicate", "enhancement",
            "help wanted", "invalid", "question", "wontfix"]
  #fetch labels
  #label_url = "https://api.github.com/repos/incognito666/tarantula-python/labels"
  #token = "559fc3d984be62f2115478b2e46385b1c1913bc6" # <===
  #request = urllib2.Request(label_url, headers={"Authorization" : "token "+token})
  #res = urllib2.urlopen(request).read()
  #labels = []
  #r = json.loads(res)
  #for l in range(0,len(r)):
   # labels.append(str(r[l]['name']))
    
  #f = open("Data_Output.txt", "r")
  f=open("projectscrapping_Data_Output.txt","r")
  long_update=[]
  line = f.readline()
  while line:
      #print(line)
##      print("---------------")
      if "ISSUE" in line:
	  issue=line[6:-1]
	  #print issue
      target = line.find("when")
      target1=line.find("updated")
      if target != -1:
          start = line.find(":",target)
          end = line.find(",",start)
          substr = float(line[start+2:end])
	  #print len(substr)
	  #print substr
      if target1 != -1:
          start1 = line.find(":",target1)
          end1 = line.find(",",start1)
          substr1 = float(line[start1+2:end1])
          #print len(substr)
          #print substr1
          if(substr1-substr>1000000):
		long_update.append(issue)
 	

      line = f.readline()
  if len(long_update)!=0:
	print "\nThe following are issues with long time to get updated:\n"
	print set(long_update)
	
	print "Total: " +  str(len(set(long_update)))
	print "Badsmell detected"

  else:
        print "All Issues have been well updated in timen\n"

  f.close()
  
findFeature()
