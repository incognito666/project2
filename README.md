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
  - This is a manual task. Each project contributors and contributions are checked. The number of commits are noted down.  
 
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
 
6. Milestones not met on time.
  - For this task, we extract the milestone due date and the milestone closed time from the data output files.  
  - Link: https://github.com/incognito666/project2/blob/master/badsmell_6.py
  
7. Most of the commits are close to the submission dates. 
  - This is a manual task. We check the commit logs and the dates of submissions.   
 
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
  - Link:https://github.com/incognito666/project2/blob/master/badsmell_13.py

14. No update in the issues for a long time.
  - We extract created time, updated time for each issue.  
  - Link: https://github.com/incognito666/project2/blob/master/badsmell_14.py

15. Labels are applied and immediately removed from an issue
  - For this task, the labels "what" (name of the label applied or unapplied to an issue), "action" (tells whether a label as been applied or unapplied to an issue), and "when" (the time of each event) were used to tell when a label was applied and then taken off.  
  - Link: https://github.com/incognito666/project2/blob/master/badsmell_15.py

18. Only one step in whole development period.
  - We extract the number of labels used from the data output files.  
  - Link: https://github.com/incognito666/project2/blob/master/badsmell_18.py
 
 
22. Issues are not posted frequently.  
  - We just need to extract the time each issue was created at.  
  - Link: https://github.com/incognito666/project2/blob/master/badsmell_22.py

# Feature Detection Results  

  Name of Feature | Tarantula | Web Scraper | Mazes
  ------------- | ------- | --------- | --- 
  No of labels  |  13   |  11  |  14 
  No of milestones|   9  |    5        |  6  |
  No of issues    |   30      |    63       |  90  |

Apart from this we have also taken the start times and end times of Issues, Milestones start, close and due time.  

Milestone Created Time (s) |	Milestone Closed Time (s) |	Milestone Due Date (s)	| Milestone Total Issues
-------------------------- | ---------------- | -------- | ---------- 
1423421122	| 1424977086 |	1423976400 |	1
1424976835 |	1425138166 |	1424926800	| 6
1424976887 |	1425941525	| 1425013200 |	3


Issue Opened Time (s) |	Issue Closed Time (s) |	Issue Total Alive Time (s)
------------------ | ------------------------- | ----------------------------
1423716612 |	1424154475 |	437863
1423886852 |	1423934053 |	47201
1423886884 |	1425169392 |	1282508
1423886965 |	1427068117 |	3181152

 - Feature Design 15
    * Maze
    
| Issue | Label              | Time Label is open (seconds) |          |
|-------|--------------------|------------------------------|----------|
| 1     | help wanted        | 2655                         |          |
| 1     | feature request    | 2691                         |          |
| 2     | feature request    | 66080                        |          |
| 2     | feature dev        | 4684                         |          |
| 2     | feature QA         | 124615                       |          |
| 2     | help wanted        | 3767                         |          |
| 5     | feature request    | 102559                       |          |
| 5     | feature dev        | 160                          | Badsmell |
| 5     | feature QA         | 27507                        |          |
| 6     | feature request    | 175687                       |          |
| 6     | feature dev        | 188719                       |          |
| 6     | feature dev        | 478581                       |          |
| 6     | help wanted        | 83151                        |          |
| 6     | feature QA         | 415335                       |          |
| 6     | feature dev        | 91201                        |          |
| 7     | feature request    | 697919                       |          |
| 7     | feature dev        | 472226                       |          |
| 7     | help wanted        | 15857                        |          |
| 8     | feature request    | 364451                       |          |
| 8     | feature QA         | 290326                       |          |
| 9     | feature QA         | 779671                       |          |
| 9     | feature dev        | 52573                        |          |
| 10    | feature request    | 340720                       |          |
| 10    | feature dev        | 328861                       |          |
| 11    | feature request    | 299966                       |          |
| 11    | feature dev        | 64039                        |          |
| 12    | feature dev        | 83556                        |          |
| 13    | feature request    | 3264                         |          |
| 13    | feature dev        | 198491                       |          |
| 15    | feature QA         | 202                          | Badsmell |
| 20    | feature request    | 51781                        |          |
| 20    | feature dev        | 214071                       |          |
| 20    | feature QA         | 125553                       |          |
| 21    | deployment         | 720251                       |          |
| 23    | feature QA         | 24987                        |          |
| 23    | feature dev        | 24987                        |          |
| 28    | feature request    | 198725                       |          |
| 34    | feature request    | 264481                       |          |
| 34    | feature QA         | 89198                        |          |
| 35    | 2a. feature dev    | 22977                        |          |
| 36    | 2a. feature dev    | 5330                         |          |
| 36    | 3. feature QA      | 61640                        |          |
| 37    | 2a. feature dev    | 242969                       |          |
| 38    | 2a. feature dev    | 266074                       |          |
| 39    | bug                | 4280                         |          |
| 40    | 3. feature QA      | 59287                        |          |
| 41    | 1. feature request | 642106                       |          |
| 41    | 2a. feature dev    | 33743                        |          |
| 41    | 3. feature QA      | 161672                       |          |
| 43    | 1. feature request | 60387                        |          |
| 43    | 2a. feature dev    | 8877                         |          |
| 43    | 3. feature QA      | 6462                         |          |
| 44    | 1. feature request | 188738                       |          |
| 44    | 2a. feature dev    | 346026                       |          |
| 44    | 3. feature QA      | 120137                       |          |
| 47    | 1. feature request | 1119189                      |          |
| 47    | 3. feature QA      | 6783                         |          |
| 49    | 2a. feature dev    | 30593                        |          |
| 49    | 3. feature QA      | 109177                       |          |
| 51    | 1. feature request | 599343                       |          |
| 51    | 2a. feature dev    | 16247                        |          |
| 51    | 3. feature QA      | 74227                        |          |
| 53    | 1. feature request | 330080                       |          |
| 53    | 2a. feature dev    | 50268                        |          |
| 53    | 3. feature QA      | 4599                         |          |
| 54    | 1. feature request | 23702                        |          |
| 54    | 2a. feature dev    | 3077                         |          |
| 56    | 1. feature request | 57383                        |          |
| 56    | 2a. feature dev    | 64040                        |          |
| 56    | 3. feature QA      | 26605                        |          |
| 58    | 1. feature request | 234068                       |          |
| 58    | 2a. feature dev    | 13380                        |          |
| 58    | 3. feature QA      | 96689                        |          |
| 59    | 1. feature request | 344044                       |          |
| 60    | 1. feature request | 2310                         |          |
| 61    | 1. feature request | 341461                       |          |
| 62    | 1. feature request | 363243                       |          |
| 64    | 1. feature request | 78251                        |          |
| 64    | 2a. feature dev    | 95841                        |          |
| 65    | 5. bug             | 68334                        |          |
| 68    | 1. feature request | 181449                       |          |
| 69    | 2a. feature dev    | 1117                         |          |
| 69    | 3. feature QA      | 48111                        |          |
| 70    | 1. feature request | 26589                        |          |
| 70    | 2a. feature dev    | 18376                        |          |
| 70    | 3. feature QA      | 56615                        |          |
| 71    | 1. feature request | 12851                        |          |
| 73    | 1. feature request | 22700                        |          |
| 74    | 1. feature request | 16125                        |          |
| 75    | 1. feature request | 22704                        |          |
| 75    | 2a. feature dev    | 50555                        |          |
| 75    | 3. feature QA      | 26345                        |          |
| 76    | 2a. feature dev    | 145636                       |          |
| 77    | 1. feature request | 530726                       |          |
| 79    | 2a. feature dev    | 1092                         |          |
| 81    | 2a. feature dev    | 204222                       |          |
| 82    | 1. feature request | 7606                         |          |
| 82    | 2a. feature dev    | 366                          |          |
| 82    | 3. feature QA      | 26178                        |          |
| 84    | 2a. feature dev    | 26276                        |          |
| 85    | 2a. feature dev    | 21362                        |          |
| 86    | 2a. feature dev    | 21247                        |          |
| 87    | 1. feature request | 15391                        |          |
| 88    | 2a. feature dev    | 151891                       |          |
| 89    | 2a. feature dev    | 12143                        |          |
| 89    | 3. feature QA      | 10882                        |          |
| 90    | 2a. feature dev    | 34766                        |          |
| 90    | 3. feature QA      | 451                          |          |
| 92    | 3. feature QA      | 8584                         |          |

    * Tarantula
    
| Issue | Label       | Time Label is open (seconds) |          |
|-------|-------------|------------------------------|----------|
| 20    | enhancement | 811604                       |          |
| 20    | Code        | 811604                       |          |
| 22    | Code        | 13                           | Badsmell |
| 24    | enhancement | 1729499                      |          |
| 24    | Design      | 1729499                      |          |
| 24    | Code        | 1729499                      |          |
| 26    | Design      | 701459                       |          |
| 26    | Code        | 701459                       |          |
| 27    | Design      | 702993                       |          |
| 27    | Code        | 702993                       |          |
| 27    | Code Review | 16                           | Badsmell |

    * Web Scrapping
    
| Issue | Label       | Time Label is open (seconds) |          |
|-------|-------------|------------------------------|----------|
| 5     | help wanted | 80825                        |          |
| 5     | Solved      | 2265                         |          |
| 5     | Solved      | 2269                         |          |
| 5     | bug         | 0                            | Badsmell |
| 5     | Solved      | 4                            | Badsmell |
| 15    | duplicate   | 3                            | Badsmell |
| 36    | Solved      | 7                            | Badsmell |

    * As you can see that not every issue has labels that are assigned then removed. There is no standard way of assigning labels which explains the differing labelling techniques. 
# Bad Smells Detector  

1. A large percentage of commits are not done by a single person.  
  - Looking at the contributors page in the repos you can see who has committed to the project and how much. A bad smell would be if someone took over the project and had a majority of the commits (20% or more than the expected contribution amount).  

2. There are no unused used labels for issues.  
  - The labels extracted directly from the label API are compared with the labels used in the issues. If there is any label which was not used in any of the issues, it is a bad smell.  
  - Link: https://github.com/incognito666/project2/blob/master/badsmell_2.py

3. An issue is not assigned to a single label for a long period of time.
  - For each issue a label should be assigned to it to let the contributors of the project know what phase that issue is in during development. A badsmell would be if an issue goes a long time (12 hours in our case) without having a label attached to it. 
  - Link: https://github.com/incognito666/project2/blob/master/badsmell_3.py
  
4. There are no unassigned issues.
  -The `user` fields for each issue are checked for values, if exists or not. If it is empty, that means that the issue has not been assigned to anyone. 
  - Link: https://github.com/incognito666/project2/blob/master/badsmell_4.py
  
5. The number of commits by a member is not less that 25% of the commits.
  - Looking at the contributors page in the repos you can see who has committed to the project and how much. A bad smell would be if someone did not commit close to an even share to the project. i.e. (total # of commits)/(# of contributors) give or take 5-10%.
 
6. Milestones not met on time.
  - The milestone end date is subtracted from the milestone due date. If the difference is more than one day, it is a bad smell.  
  - Link: https://github.com/incognito666/project2/blob/master/badsmell_6.py
  
7. Most of the commits are close to the submission dates. 
  - Looking at the contributors page in the repo you can see when the commits happen. A bad smell would be if there is a huge curve near the end of the deadline which will signal waiting till the last minute. 
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
  - Link: https://github.com/incognito666/project2/blob/master/badsmell_13.py

14. No update in the issues for a long time.
  - For each issue, the difference between the issue opened at and updated at time is checked if its more than usual, this implies the issue has not been updated for a long time. 
  - Link: https://github.com/incognito666/project2/blob/master/badsmell_14.py

15. Labels are applied and immediately removed from an issue
  -   For each issue we will search through the events and look to see if a label is applied. Once we find an applied label we see if that label has been removed. A badsmell would be if the label was removed within 5 minutes (which is a configurable number) showing that not much time was spent in that phase. 
  - Link: https://github.com/incognito666/project2/blob/master/badsmell_15.py

18. Only one step in whole development period.
  - If there is only one label extracted from all the issues, this implies there was only one step in the lifecycle of the project (for example-no plan or design, direct code phase) it is a bad smell.
  - Link: https://github.com/incognito666/project2/blob/master/badsmell_18.py

22. Issues are not posted frequently.  
  - The duration between each consecutive issue is calculated by subtracting their creation times (`creation_time2 - creation_time2`). The average of all these is caluclated. If any difference is greater than twice the calculated average, it is a bad smell.  
  - Link: https://github.com/incognito666/project2/blob/master/badsmell_22.py


# Bad Smells Results  

1. A large percentage of commits are not done by a single person.  
  - Tarantula  
  ![Image for Badsmell 1 - Tarantula] (https://github.com/incognito666/project2/blob/master/Contribution_p.png)  
As seen in the figure above, the commits for this project are distributed fairly evenly. 
Total Number of Commits: 60
By each member, number of commits are 15, 13, ,12, 11, 9 sorted in descending order.  


  - Web scraper  
  ![Image for Badsmell 1 - Tarantula] (https://github.com/incognito666/project2/blob/master/Contribution_w.png)  
From the figure, we can observer that there is quite a big difference in the number of commits between A and C.  
Total Number of Commits: 455
By each member, number of commits are 193, 180, 62, 38 sorted in descending order.  

  - Maze  
  ![Image for Badsmell 1 - Tarantula] (https://github.com/incognito666/project2/blob/master/Contribution_m.png)  
From the figure, we can observer that there is quite a big difference in the number of commits between A, C and D.  
Total Number of Commits: 378
By each member, number of commits are 151, 127, ,82 sorted in descending order.  

 
2. There are no unused used labels for issues. 
  ![Image for Badsmell 2 - Tarantula] (https://github.com/incognito666/project2/blob/master/graph/badsmell_2_tarantula.png)  

  ![Image for Badsmell 2 - Web Scraper] (https://github.com/incognito666/project2/blob/master/graph/badsmell_2_webscraper.png)  
  
  ![Image for Badsmell 2 - Mazes] (https://github.com/incognito666/project2/blob/master/graph/badsmell_2_mazes.png) 
  
3. An issue is not assigned to a single label for a long period of time.
  - Tarantula  
  ![Image for Badsmell 3 - Tarantula] (https://github.com/incognito666/project2/blob/master/PythonTarantula/BS3.png)  
From the Graph you can see that there are 7 instanced where a Issue went over 12 hours without having a label. This could be a slight problem for a project with 30 Issues. The initial Issues can be excused since adding labels was not specified at first. But having a bunch of Issues without labels shows disorganization which can lead to uncertainty and delivery slip of certain features and the product. You could fix it by having another developer review your issues once created.  


  - Web scraper  
  ![Image for Badsmell 3 - Web scraper] (https://github.com/incognito666/project2/blob/master/WebScraping/BS3.png)  
From the Graph you can see that there are 3 instanced where a Issue went over 12 hours without having a label. This is fairly good for a project with 69 Issues. This shows that there was structure and a good flow. If this was a problem, you could fix it by having another developer review your issues once created. 

  - Maze  
  ![Image for Badsmell 3 - Maze] (https://github.com/incognito666/project2/blob/master/Maze/BS3.png)  
From the Graph you can see that there are 2 instanced where a Issue went over 12 hours without having a label. This is fairly good for a project with 93 Issues. This shows that there was structure and a good flow. If this was a problem, you could fix it by having another developer review your issues once created.    

4. There are no unassigned issues.
   
   For the projects Tarantula in python, project scraping and Maze generation all the issues have been assigned. Hence this bad smell was not visible in any of these projects. But if this was an issue you could resolve this by having a person (Manager of some sort) responsible for checking the issues frequently to see if there are issues that may have not been assigned to anyone.  

5. The number of commits by a member is not less that 25% of the commits.
 
   Looking at the graphs in #1. 
   - Tarantula  
 
   Total Number of Commits: 60
   By each member, number of commits are 15, 13, 12, 11, 9 sorted in descending order. You can see that each person should have about 12 Commits each. The lowest person has 9 commits which is less than 12 and could be flagged as a bad smell but the commits are fairly even. 


   - Web scraper  
  
   Total Number of Commits: 455
   By each member, number of commits are 193, 180, 62, 38 sorted in descending order. You can see that each person should have about 114 Commits each. The lowest person has 38 commits which would be a huge red flag. To fix this one could try and break up the features evenly. This could also be the outcome of having a group member who just commits multiple times a day then there is no problem really. 

   - Maze  
 
   Total Number of Commits: 378
   By each member, number of commits are 151, 127, 82 sorted in descending order. You can see that each person should have about 126 Commits each. The lowest person has 82 commits which would be a bad smell. To fix this one could evenly distribute the features or have the code reviewers submit the code.  

6. Milestones not met on time.
   ![Image of Badsmell 6] (https://github.com/incognito666/project2/blob/master/graph/badsmell_6.png)  

7. Most of the commits are close to the submission dates.  

   Looking at the graphs in #1, you can see that in all 3 repos that there are a large number of submits towards the end of the submission date. This could mainly be how Grad Students work. Also working with a group of people you may not have worked with before may also contribute to the rush at the end. To solve this just try to set up better due dates based off of your abilities. Ff you have a feature that is pretty big you should try to break it up into smaller more manageable pieces that can be split between multiple people.   

8. All the issue  have not been resolved.   
    For the projects Tarantula in python, project scraping and Maze generation all the issues have been closed. Hence this bad smell was not visible in any of these projects


9. Issues are not closed on time.
  ![Image for Badsmell 9] (https://github.com/incognito666/project2/blob/master/graph/badsmell_9.png)  

10. Some issues have been open for too long. 
  - Tarantula  
  ![Image for Badsmell 3 - Tarantula] (https://github.com/incognito666/project2/blob/master/PythonTarantula/BS10.png)  
From the Graph you can see that there are 4 instanced where a Issues lasted twice as long as the average. These Issues are spaced out so there isn't a pattern that you can see. This could just be where a few of the harder or more intensive features got put in. To avoid this in the future I would break down those issues into smaller issues to help knock those out quickly. 


  - Web scraper  
  ![Image for Badsmell 3 - Web scraper] (https://github.com/incognito666/project2/blob/master/WebScraping/BS10.png)  
From the Graph you can see that there are 13 instanced where a Issues lasted twice as long as the average. The bad smells seem bunched up. This could just be where a lot of the harder or more intensive features got put in. To avoid this in the future I would break down those issues into smaller issues to help knock those out quickly. 

  - Maze  
  ![Image for Badsmell 3 - Maze] (https://github.com/incognito666/project2/blob/master/Maze/BS10.png)  
From the Graph you can see that there are 14 instanced where a Issues lasted twice as long as the average. The bad smells seem bunched up. This could just be where a lot of the harder or more intensive features got put in. To avoid this in the future I would break down those issues into smaller issues to help knock those out quickly. 
  
11. No issues in the milestone.  
   ![Image for Badsmell 11] (https://github.com/incognito666/project2/blob/master/graph/badsmell_11.png)  

12. Just one issue in the milestone.
   
   The following graph has been plotted for the three projects indicating the number of bad smells.

   ![Image for Badsmell12] (https://github.com/incognito666/project2/blob/master/graph/badsmell_12.png)
   
   The X axis of the graph indicates the project number where they represent, tarantula in python, Project scrapping and Maze generation accordingly.

   The Y axis indicates the number of issues having this bad smell. The green bar in the histogram indicates the bad smells.

13. Lack of communication in the issues.

  The following graph has been plotted for the three projects indicating the number of bad smells and the number of really bad smells.
   
   ![ImageforBadsmell13] (https://github.com/incognito666/project2/blob/master/graph/badsmell_13_graph.png)

  The X axis of the graph indicates the project number where they represent, tarantula in python, Project scrapping and Maze generation accordingly.   

  The Y axis indicates the number of issues having this bad smell.The blue bar in the histogram indicates the really bad smells and the red bar indicates the bad smells.

14. No update in the issues for a long time.
    
    The following graph has been plotted for the three projects indicating the number of bad smells.

    ![Image for Badsmell14] (https://github.com/incognito666/project2/blob/master/graph/badsmell_14.png)

    The X axis of the graph indicates the project number where they represent, tarantula in python, Project scrapping and Maze generation accordingly.

    The Y axis indicates the number of issues having this bad smell. The blue bar in the histogram indicates the bad smells.

15. Labels are applied and immediately removed from an issue
  - Tarantula  
In the tables shown in the Feature Detection Results, you can see that there are 2 instances of a bad smell. These can be resolved by having a better schedule and distributing the work better.    


  - Web scraper  
In the tables shown in the Feature Detection Results, you can see that there are 4 instances of a bad smell. These labels are secondary labels which can be done quickly. 

  - Maze  
In the tables shown in the Feature Detection Results, you can see that there are 2 instances of a bad smell. These instances could just be a lapse in memory of keeping track the progress and can be resolved with having someone check that the issues are up to date or have a regular meeting (scrum) to go over the open issues. 

18. Only one step in whole development period.
  ![Image for Badsmell 18] (https://github.com/incognito666/project2/blob/master/graph/badsmell_18.png)  

22. Issues are not posted frequently. 
  ![Image for Badsmell 22] (https://github.com/incognito666/project2/blob/master/graph/badsmell_22.png)  


# Early Warning  


We have 2 scripts for detecting bad smells early. The code for both of these is combined in a single file.  

1. Graph of Issue Created times and trendline  

  The code first finds out the creation times of all the issues that were created. The data is them sorted chronologically and kept in a list for plotting on the graph.  
  While plotting the graphs, we plot (time the issue was created - time the first issue was created) on the Y axix and the issues along the x axis. The reason to subtract it from the time on the first issue is to get the relative time it took to create each issue. This graph gives us many points of observation like 
  - If you have a horizontal line, all issues on that line were created together
  - If you have a steep slope, it shown that there was a huge gap wherein no issues were created
All these things are good but they could mean good as well as bad things, for eg. the issues created together could be during a review phase while the steep slope could mean that either there was no work done at all or it was a requirement gathering phase in an agile environment.  

To help predict the bad smell at an early stage, we plot a polynomial trend line of the second order on the data present. This trendline will let us know the amount of issues that could be created later on. Also, the trendline gives us the baseline with with we can measure the relative progress. If the number of issues created go above the trendline, it means that the project is facing more issues and that could delay the project resulting in a bad smell.  

2. Time taken between closing consecutive issues compared to a fixed value of 7 days  
  The code finds out the time that each issue was closed. The data is then sorted and kept in a list for plotting on a graph. After that, we find the difference between the issue clsoe time and the close time of the issue chronologically closed before it. This data gives us the time taken between consecutive issues. We compare it with a baseline of 7 days (Since the project was about 2 months long). If no consecutive issues are closed within 7 days of each other, we can see that a slack is getting introduced in the project. The could mean that the team is not working at full potential and it might result in delaying a project.  

[Link to Script] (https://github.com/incognito666/project2/blob/master/earlyDetection.py)  

# Early Warning Results  

1. Graph of Issue Created times and trendine  

  - Tarantula  
    ![Image of issue created time] (https://github.com/incognito666/project2/blob/master/graph/extra_created_tarantula.png)  
    Here we can see that after issue no 17, there seemed to be a point where we could say that the project was going through a rough phase.  
   
  - Web Scraper  
    ![Image of issue created time] (https://raw.githubusercontent.com/incognito666/project2/master/graph/extra_created_webscraper.png)  
 Here we can see that there are 2 very distinct phases in the project with the second one being turbulet.  

  - Mazes  
    ![Image of issue created time] (https://raw.githubusercontent.com/incognito666/project2/master/graph/extra_created_mazes.png)  
Here we see a similar trend but in the middle of the project.  

2. Time taken between closing consecutive issues compared to a fixed value of 7 days  

  - Tarantula
  
  ![Image of end time] (https://github.com/incognito666/project2/blob/master/graph/extra_ended_tarantula.png)  

  - Web Scraper  
  ![Image of end time] (https://github.com/incognito666/project2/blob/master/graph/extra_ended_webscraper.png)  

  - Mazes  
  ![Image of end time] (https://github.com/incognito666/project2/blob/master/graph/extra_ended_mazes.png)  
