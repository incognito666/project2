import urllib2
import json

def findFeature():
  f = open("Data_Output.txt", "r")

  line = f.readline()
  issue_no = 0
  while line:
##      print(line)
##      print("---------------")

      m_total = line.find("milestone_total")
      if m_total == -1:
          line = f.readline()
          continue
      start = line.find(":",m_total)
      end = line.find(",",start)
      cnt = line[start+2:end]
      if cnt == "0":
          print("Bad Smell found -- Milestone has 0 issues assigned")
          break
      line = f.readline()
  f.close()
  
findFeature()
