import urllib2
import json

def findFeature():
  f = open("Data_Output3.txt", "r")
  c=0
  line = f.readline()
  issue_no = 0
  m_names=[]
  count=0
  while line:
      count=count+1
##      print(line)
##      print("---------------")

      m_total = line.find("milestone_total")
      if m_total == -1:
          line = f.readline()
          continue
      name_total = line.find("milestone_name")
      if name_total != -1:
##          line = f.readline()
##          continue
          name_start = line.find(":",name_total)
          name_end = line.find(",",name_start)
          name=line[name_start+2:name_end]
          if name not in m_names:
              m_names.append(name)
      
      
              start = line.find(":",m_total)
              end = line.find(",",start)
              
              cnt = line[start+2:end]
              print cnt.strip()
              print cnt.strip() is "0"
              if cnt.strip() is "0":# and name not in m_names:
                  print name
                  
                  c=c+1
                  print("Bad Smell found -- Milestone has 0 issues assigned")
      line = f.readline()
  print "no of milestones with 0 assigned issues",c
  print "total no of milestones",len(m_names)
  f.close()
  
findFeature()
