import urllib2
import json

def findFeature():
  late_issues = []
  covered_issues = []
  unassigned_issues = {}
  running_avg = 0
  count = 0
  f = open("Data_Output3.txt", "r")
  diff=[]
  line = f.readline()
  issue_no = 0
  sum1=0
  while line:
##      print(line)
##      print("---------------")
      if line.startswith("ISSUE"):
          print "issue line ",line[6:]
          issue_no = line[6:].strip()   # line = ISSUE <Number>
          
          line  = f.readline()
          count+=1
          continue
      if issue_no in covered_issues:
          line = f.readline()
          continue
      ended = line.find("ended")
      if ended is -1  or issue_no in covered_issues:
          line  = f.readline()
          continue
      ended_start = line.find(":",ended)
      ended_end = line.find(",",ended_start)
      end_time = line[ended_start+1:ended_end].strip()
##      print "End time:"
##      print(end_time)
      if end_time == "0":
        late_issues.append(issue_no)
        covered_issues.append(issue_no)
        line  = f.readline()
        continue
        

      issue_created = line.find("opened")
      issue_end = line.find(",",issue_created)
      issue_crtd = line[issue_created+8:issue_end]
      temp=float(end_time)-float(issue_crtd)
      diff.append(temp)
      sum1+=temp
      covered_issues.append(issue_no)


##      isMilestoneAssigned = line.find("milestone_due")
##      start = line.find(":",isMilestoneAssigned)
##      end = line.find(",",start)
##      substr = line[start+2:end].strip()
##      print "Milestone due is ",substr 
####      running_avg+= float(end_time) - float(issue_crtd)
##      if substr is not "0" and substr is not "None":
##          print "here"
##          if substr is not None:
##            print "Time Taken ",float(end_time) - float(substr)
##            if end_time == "0" or (float(end_time) - float(substr)) >= 86400:
##                late_issues.append(issue_no)
##      else:
##          print "not found"
##          unassigned_issues[issue_no] = float(end_time) - float(issue_crtd)
##      covered_issues.append(issue_no)


      line  = f.readline()
##  print(unassigned_issues)
##  print("Late issues are ")
##  print late_issues
  print "Cobered issue len ",len(covered_issues)
  print(diff)# = []
  avg=sum1/len(diff)
  print("avg is",avg)
  f.close()
  badsmell=0
  for i in diff:
    if i>2*avg:
##      print 
      badsmell+=1
  if badsmell>1:
    print("you stink",badsmell,"no of issues",len(diff))
findFeature()
