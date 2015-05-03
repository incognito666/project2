import urllib2
import json

def findFeature():
##  label_url = "https://api.github.com/repos/SuperCh-SE-NCSU/ProjectScraping/labels"
##  label_url = "https://api.github.com/repos/incognito666/tarantula-python/labels"
  label_url = "https://api.github.com/repos/CSC510-2015-Axitron/maze/labels"
  token = "INSERT TOKEN HERE" # <===
  request = urllib2.Request(label_url, headers={"Authorization" : "token "+token})
  res = urllib2.urlopen(request).read()
  labels = []
  r = json.loads(res)
##  r = json.loads(res)
  print "r ",r

  for l in range(0,len(r)):
    labels.append(str(r[l]['name']))
  if len(labels) is 1:
    print "Bad Smell Found"
##        break
  else:
    print "no bad smell"
      
findFeature()
