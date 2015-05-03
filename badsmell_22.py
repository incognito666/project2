import urllib2
import json

def findFeature():
  covered_issues = []
  start_times = []
  running_avg = 0
  count = 0
  badsmell=0
  f = open("Data_Output.txt", "r")
  line = f.readline()
  issue_no = ''
  while line:
##      print(line)
##      print("---------------")
      if line.startswith("ISSUE"):
##          print("issue line")
          issue_no = line[6:].strip()   # line = ISSUE <Number>
          line  = f.readline()
          continue
      if issue_no in covered_issues:
          line  = f.readline()
          continue
      issue_created = line.find("when")
      issue_end = line.find(",",issue_created)
      issue_crtd = line[issue_created+6:issue_end]
      if issue_created is not -1:
          start_times.append(issue_crtd.strip())
          covered_issues.append(issue_no)
      line  = f.readline()

  print(covered_issues)
  sorted_times = sorted(start_times)
##  print(sorted_times)
  print(start_times)
##  print(len(sorted_times))
  f.close()
  diff=[]
  sum1=0
  for i in range(0,len(sorted_times)-1):
      temp=float(sorted_times[i+1])-float(sorted_times[i])
      diff.append(temp)
      sum1=sum1+temp
##  print ("diffs")
##  print(diff)
  avg=sum1/len(sorted_times)
  print("avg is",avg)
  for  j in diff:
      if j>2*avg:
          badsmell+=1
  if badsmell>1:
      print("you stink!!!",badsmell)
findFeature()
