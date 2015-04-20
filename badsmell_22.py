import urllib2
import json

def findFeature():
  covered_issues = []
  start_times = []
  issue_no = 0
  running_avg = 0
  count = 0
  f = open("Data_Output.txt", "r")

  line = f.readline()
  issue_no = 0
  while line:
##      print(line)
##      print("---------------")
      if line.startswith("ISSUE"):
          print("issue line")
          issue_no = line[6:].strip()   # line = ISSUE <Number>
          line  = f.readline()
          continue
      if issue_no in covered_issues:
          line  = f.readline()
          continue
      issue_created = line.find("when")
      issue_end = line.find(",",issue_created)
      issue_crtd = line[issue_created+6:issue_end]
      start_times.append(issue_crtd)
      covered_issues.append(issue_no)
      line  = f.readline()

  print(covered_issues)
  print(start_times)
  f.close()
  
findFeature()
