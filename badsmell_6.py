import urllib2
import json

def findFeature():
    f = open("Data_Output.txt", "r")
    i=0
    line = f.readline()
    name=[]
    badsmell=0
    while line:
##        print line 
        print("---------------")
        
        
        milestone_name=line.find("milestone_name")
        if milestone_name is -1:
            line = f.readline()
            continue
        start = line.find(":",milestone_name)
        end = line.find(",",start)
        temp=line[start+1:end]
##        name[i]=temp
##        print "namesssss",temp
        if temp not in name:
            name.append(temp)
                    
            print name
            due=0
            target=line.find("milestone_due")
            if target!=-1:
                start = line.find(":",target)
                end = line.find(",",start)
                due = line[start+1:end]
                print "**********"
                print due
            target=line.find("milestone_closed")
            closed=0
            if target!=-1:
                start = line.find(":",target)
                end = line.find(",",start)
                closed = line[start+1:end]
                print "**********"
                print closed
            if closed == 'None' or due == 'None':
                badsmell=badsmell+1
                print "something is none!!!!!!!!!!!!"
                pass
            time=float(closed)-float(due)
            if time>86400:
                badsmell=badsmell+1

        line = f.readline()
        i=i+1
    if badsmell>0:
        print "badsmells!!!you stink!",badsmell
findFeature()
