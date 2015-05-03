import urllib2
import json

def findFeature():
  ##1. all labels are used
##  labels = ["Design","Code","Unit Test", "Integration Test",
##            "Code Review", "Recover", "bug", "duplicate", "enhancement",
##            "help wanted", "invalid", "question", "wontfix"]
  #fetch labels
##  label_url = "https://api.github.com/repos/SuperCh-SE-NCSU/ProjectScraping/labels"
##  label_url = "https://api.github.com/repos/incognito666/tarantula-python/labels"
  label_url = "https://api.github.com/repos/CSC510-2015-Axitron/maze/labels"
  token = "INSERT TOKEN HERE" # <===
  request = urllib2.Request(label_url, headers={"Authorization" : "token "+token})
  res = urllib2.urlopen(request).read()
  labels = []
  r = json.loads(res)

  for l in range(0,len(r)):
    labels.append(str(r[l]['name']))
    
  f = open("Data_Output3.txt", "r")
  print("All the labels are: ")
  print(labels)

  line = f.readline()
  while line:
##      print(line)
##      print("---------------")
      target = line.find("what")
      if target != -1:
          start = line.find(":",target)
          end = line.find(",",start)
          substr = line[start:end]
          for label in labels:
              if substr.find(label) is not -1:
                  labels.remove(label)
      line = f.readline()
  print("The following labels are unused")
  print(labels)
  if len(labels) != 0:
      print("Bad smell detected")
  f.close()
  
findFeature()
