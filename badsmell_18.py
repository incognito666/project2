import urllib2
import json

def findFeature():
  token = "604a29fab94b418dfc53ac3f61056e176c6d6352" # <=== new token
  request = urllib2.Request(label_url, headers={"Authorization" : "token "+token})
  res = urllib2.urlopen(request).read()
  labels = []
  r = json.loads(res)

  for l in range(0,len(r)):
    labels.append(str(r[l]['name']))
    if len(labels) is 1:
        print "Bad Smell Found"
        break
 
      
