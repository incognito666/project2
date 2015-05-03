import string, os, sys

def issue_duration():
    f=open("Data_Output_p.txt", "r")
    lines = f.readlines()
    index = 0
    issue_durations = {}
    print('Issue,Active Issue Time (seconds)')
    av_Sum = 0
    av_Num = 0
    for line in lines: 
        if line.startswith("ISSUE"): 
            blank_line_index = 0
            issue_array = []
            for blank_search in range(index+1, len(lines)):
                if not lines[blank_search].strip():
                    blank_line_index = blank_search                    
                    break            
            if blank_line_index == 0:
                print("Issue has no events")
                continue            
            for event_search in range(1, blank_line_index - index):
                issue_array.append(lines[blank_line_index - event_search])
            
            a_index = issue_array[0].find("alive :")           
            a_string = issue_array[0][a_index + 8:issue_array[0].find(',',a_index)]
            #print(a_string)
            if a_string != '-1': 
                av_Num += 1
                av_Sum += int(float(a_string))
                issue_durations[line[6:-1]] = int(float(a_string))
                #print("   "+str(av_Num)+":"+str(av_Sum))
        index = index + 1 
    average = av_Sum/av_Num
    for key in issue_durations:
        out_string = key+','+str(issue_durations[key])
        if issue_durations[key] > average*2:
            out_string = out_string+',Badsmell'
        print(out_string)
    print('')
    print(average)
issue_duration()