# Project 2: Bad Smell and Feature Extractor
CSC 510  
Software Engineering

# 1.Collection  

We are using the already provided gitable.py with few modifications.  
We have modified gitable to include some information from the Github API, write the data into a text file with comma separated values, and added our anonymization logic.  

# 2.Anonymization   

We use a simple replacement algorithm for anonymizing the data; every unique name in the project repo is replaced by an alphabet.  


```python  
if user not in users.keys():    
      users[user] = chr(name_i)  
      name_i+=1     
user = users[user]  
```   

`name_i` has been initialized with 65. Hence, `chr(name_i)` will give us the character of that ASCII integer.    

# 3.Tables  

To place the data that we retrieved from the repos into a table we created a script named [table_gen.py] (https://github.com/incognito666/project2/blob/master/table_gen.py)  which parsed the data for the name of the attribute (i.e. "opened :" and "milestone_name :") to get the value of it and placed that value into a csv formatted table.  

The csv table for each repo we did are located at:

1) [Tarantula in Python] (https://github.com/incognito666/project2/blob/master/Data_Table_p.csv)    
2) [Web Scraper] (https://github.com/incognito666/project2/blob/master/Data_Table_w.csv)    
3) [Maze] (https://github.com/incognito666/project2/blob/master/Data_Table_m.csv) 

The columns specify the attribute while the rows are the events which are grouped by issue and sorted from earliest to latest event for that issue. 

The other tables created in this report follow the same data parsing structure. 

# Data   

We are detecting bad smells from three projects:  

1) [Tarantula in Python] (https://api.github.com/repos/incognito666/tarantula-python/issues/)    
2) [Web Scraper] (https://api.github.com/repos/SuperCh-SE-NCSU/ProjectScraping/issues/)    
3) [Maze] (https://api.github.com/repos/CSC510-2015-Axitron/maze/issues/)     

For each project, we collected the following data:  
- The issue number
- When the milestones (that a particular issue was assigned to) were closed
- The total number of issues that were assigned a particular milestone
- When a issue was opened
- The name of the issue
- When each milestone was created
- The name of each milestone
- When each milestone was updated
- The number of comments per milestone
- When the milestone was closed
- When the milestone was due
- How long a milestone was 'alive'  

# Data Samples  

When gitable_27.py (our modified version of gitable.py) is executed for each project, all the data is redirected into a comma separated text file.    

[Data_Output.txt for Tarantula] (https://github.com/incognito666/project2/blob/master/Data_Output.txt)      
[Data_Output2.txt for Web Scraper] (https://github.com/incognito666/project2/blob/master/Data_Output2.txt)   
[Data_Output3.txt for Maze] (https://github.com/incognito666/project2/blob/master/Data_Output3.txt)  

A typical issue in the data output files is as below:
```
ISSUE 2
milestone_closed : 1425138166.0,	milestone_total : 6,	opened : 1423886852.0,	what : question,	milestone_created : 1424976835.0,	milestone_name : Get coverage code up and running,	when : 1423943521.0,	updated : 1424977031.0,	comments : 1,	ended : 1423934053.0,	milestone_due : 1424926800.0,	user : C,	action : labeled,	alive : 47201.0
milestone_closed : 1425138166.0,	milestone_total : 6,	opened : 1423886852.0,	what : Design,	milestone_created : 1424976835.0,	milestone_name : Get coverage code up and running,	when : 1423943515.0,	updated : 1424977031.0,	comments : 1,	ended : 1423934053.0,	milestone_due : 1424926800.0,	user : C,	action : labeled,	alive : 47201.0
```

# Feature Detection  

NOTE: Our feature extractor and bad smell detectors are not specified separately. For each bad smell, the corresponding features are extracted and then the code for bad smell detection is executed.  

1. A large percentage of commits are not done by a single person.  
  - This is a manual task. Each project contributors and contributions are checked. The number of commits for each project are shown at [PythonTarantula] (https://github.com/incognito666/project2/blob/master/Contribution_p.png),[Maze] (https://github.com/incognito666/project2/blob/master/Contribution_m.png) and [ProjectScraping] (https://github.com/incognito666/project2/blob/master/Contribution_w.png) 
  -  
 
2. There are no unused used labels for issues.  
  - For this task, the labels per issue are needed (from the data output file). Also required are all the labels of that project. This is extracted from the [label API] (https://api.github.com/repos/CSC510-2015-Axitron/maze/labels).  
  - Link: https://github.com/incognito666/project2/blob/master/badsmell_2.py

3. An issue is not assigned to a single label for a long period of time.
  - For this task, the labels "opened" (the time at which the issue was created) and "when" (the time of each event) for the first event are used to get the time at which the issue did not have a label.   
  - Link: https://github.com/incognito666/project2/blob/master/badsmell_3.py
  
4. There are no unassigned issues.
  - The value of `user` field is extracted for each issue.   
  - Link: https://github.com/incognito666/project2/blob/master/badsmell_4.py
  
5. The number of commits by a member is not less that 25% of the commits.
  - This is a manual task. Each project contributors and contributions are checked. The number of commits are noted down.  
  - Link: 
 
6. Milestones not met on time.
  - For this task, we extract the milestone due date and the milestone closed time from the data output files.  
  - Link: https://github.com/incognito666/project2/blob/master/badsmell_6.py
  
7. Most of the commits are close to the submission dates. 
  - This is a manual task. We check the commit logs and the dates of submissions.  
  - Link: 
 
8. Issues have not been resolved.
  - The issue closed time is checked for each issue.   
  - Link: https://github.com/incognito666/project2/blob/master/badsmell_8.py
  
9. Issues are not closed on time.  
  - The issue created and issue closed dates are extracted from the data output files.  
  - Link: https://github.com/incognito666/project2/blob/master/badsmell_9.py
 
10. Some issues have been open for too long. 
  - For this task, the alive parameter for each issue is collected. This parameter is the difference between "ended" (Time as which the issue is opened) and "opened" (Time as which the issue is opened) to give use the total time the issue was active. 
  - Link: https://github.com/incognito666/project2/blob/master/badsmell_10.py
  
11. No issues in the milestone.  
  - We extract the total number of issues assigned to each milestone.  
  - Link: https://github.com/incognito666/project2/blob/master/badsmell_11.py

12. Just one issue in the milestone.
  - We extract the total number of issues assigned to each milestone.  
  - Link: https://github.com/incognito666/project2/blob/master/badsmell_12.py

13. Lack of communication in issues.
  - We extract the comments field from the data output files.  
  - Link: 

14. No update in the issues for a long time.
  - We extract created time, updated time for each issue.  
  - Link: https://github.com/incognito666/project2/blob/master/badsmell_14.py

15. Labels are applied and immediately removed from an issue
  - For this task, the labels "what" (name of the label applied or unapplied to an issue), "action" (tells whether a label as been applied or unapplied to an issue), and "when" (the time of each event) were used to tell when a label was applied and then taken off.  
  - Link: https://github.com/incognito666/project2/blob/master/badsmell_15.py

18. Only one step in whole development period.
  - We extract the number of labels used from the data output files.  
  - Link: https://github.com/incognito666/project2/blob/master/badsmell_18.py
 
19. God class.  
  - This is a manual task. No feature can be extracted for this. We need to go to the repo and look at the project files.  
 
22. Issues are not posted frequently.  
  - We just need to extract the time each issue was created at.  
  - Link: https://github.com/incognito666/project2/blob/master/badsmell_22.py

# Feature Detection Results  

graphs here?  
  
# Bad Smells Detector  

1. A large percentage of commits are not done by a single person.  
  - 
 
2. There are no unused used labels for issues.  
  - The labels extracted directly from the label API are compared with the labels used in the issues. If there is any label which was not used in any of the issues, it is a bad smell.  
  - Link: https://github.com/incognito666/project2/blob/master/badsmell_2.py

3. An issue is not assigned to a single label for a long period of time.
  - For each issue, we take the time that the issue was created and subtract that from the first event. Since each event that we have captured in the data corresponds to a label event this subtraction gives us a rough estimate to when a label was applied. A badsmell for us would be if there was no label applied to an issue for more than 12 hours which seemed more than long enough to apply a label to an issue. 
  - Link: https://github.com/incognito666/project2/blob/master/badsmell_3.py
  
4. There are no unassigned issues.
  -The `user` fields for each issue are checked for values, if exists or not. If it is empty, that means that the issue has not been assigned to anyone. 
  - Link: https://github.com/incognito666/project2/blob/master/badsmell_4.py
  
5. The number of commits by a member is not less that 25% of the commits.
  - 
 
6. Milestones not met on time.
  - The milestone end date is subtracted from the milestone due date. If the difference is more than one day, it is a bad smell.  
  - Link: https://github.com/incognito666/project2/blob/master/badsmell_6.py
  
7. Most of the commits are close to the submission dates. 
  - 
  - Link: https://github.com/incognito666/project2/blob/master/badsmell_7.py

8. All the issue  have not been resolved.
  - After getting the closed times for all the issues, we check if there is a closed time or not. If that field is empty it means the issue has not been closed or resolved.  
  - Link: https://github.com/incognito666/project2/blob/master/badsmell_8.py
  
9. Issues are not closed on time.  
  - The duration of each issue is calculated by subtracting the issue closed time from the issue created time. The average of all these durations is calculated. If there is any duration that is two times more than this average, it is a bad smell.  
  - Link: https://github.com/incognito666/project2/blob/master/badsmell_9.py
 
10. Some issues have been open for too long. 
  - For each issue, we capture the total time the issue was active. We find the average time an issue is opened and if an issue is open longer than 2 times the average time then that will signal a bad smell. 
  - Link: https://github.com/incognito666/project2/blob/master/badsmell_10.py
  
11. No issues in the milestone.  
  - For each issue, the `milestone_total` tag is checked; if it is zero that means no issues were assigned to this milestone and this is reported as bad smell.   
  - Link: https://github.com/incognito666/project2/blob/master/badsmell_11.py

12. Just one issue in the milestone.
  - For each issue, the `milestone_total` tag is checked; if the value is one, it is a bad smell. 
  - Link: https://github.com/incognito666/project2/blob/master/badsmell_12.py

13. Lack of communication in the issues.
  - For each issue, we check the comments and the question field. If there are no comments it means lack of communication and if the question field is empty, its considered as really bad smell.  
  - Link: 

14. No update in the issues for a long time.
  - For each issue, the difference between the issue opened at and updated at time is checked if its more than usual, this implies the issue has not been updated for a long time. 
  - Link: https://github.com/incognito666/project2/blob/master/badsmell_14.py

15. Labels are applied and immediately removed from an issue
  - For each issue we will search through the events and look to see if a label is applied. Once we find an applied label we see if that label has been removed. A badsmell would be if the label was removed within 5 minutes (which is a configurable number) showing that not much time was spent in that phase. 
  - Link: https://github.com/incognito666/project2/blob/master/badsmell_15.py

18. Only one step in whole development period.
  - If there is only one label extracted from all the issues, this implies there was only one step in the lifecycle of the project (for example-no plan or design, direct code phase) it is a bad smell.
  - Link: https://github.com/incognito666/project2/blob/master/badsmell_18.py
 
19. God class.  
  - 
 
22. Issues are not posted frequently.  
  - The duration between each consecutive issue is calculated by subtracting their creation times (`creation_time2 - creation_time2`). The average of all these is caluclated. If any difference is greater than twice the calculated average, it is a bad smell.  
  - Link: https://github.com/incognito666/project2/blob/master/badsmell_22.py


# Bad Smells Results  

# Early Warning  

//scripts, description, links to code  

# Early Warning Results  





