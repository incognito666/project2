##Extra credit - early detection

import urllib2
import json

def findFeature():
  late_issues = []
  covered_issues = []
  end_times = []
  start_times = []
  count = 0
  f = open("Data_Output.txt", "r")
  diff=[]
  line = f.readline()
  issue_no = 0
  while line:
      if line.startswith("ISSUE"):
          issue_no = line[6:].strip()   # line = ISSUE <Number>
          line  = f.readline()
          count+=1
          continue
      ended = line.find("ended")
      if ended is -1  or issue_no in covered_issues:
          line  = f.readline()
          continue
      ended_start = line.find(":",ended)
      ended_end = line.find(",",ended_start)
      end_time = line[ended_start+1:ended_end].strip()
      if end_time == "0":
        late_issues.append(issue_no)
        covered_issues.append(issue_no)
        line  = f.readline()
        continue
      end_times.append(end_time)
      covered_issues.append(issue_no)
      issue_created = line.find("when")
      issue_end = line.find(",",issue_created)
      issue_crtd = line[issue_created+6:issue_end]
      start_times.append(issue_crtd)
      line  = f.readline()
  f.close()
  print "end times ",str(end_times)
  print "Len is ",len(end_times)
  print "################"
  print "start times ",str(start_times)
  print "Len is ",len(start_times)
  end_times.sort()
  for i in range(1,len(end_times)-1):
      diff.append(float(end_times[i])-float(end_times[i-1]))
  print "Diff is ",str(diff)
findFeature()
