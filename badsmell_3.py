import string, os, sys

def naked_issue():
    f=open("Data_Output.txt", "r")
    lines = f.readlines()
    index = 0
    no_label_time = {}
    print('Issue,Time with no Label(seconds)')
    for line in lines: 
        if line.startswith("ISSUE"): 
            #print(line[:-1])
            blank_line_index = 0
            issue_array = []
            for blank_search in range(index+1, len(lines)):
                if not lines[blank_search].strip():
                    blank_line_index = blank_search                    
                    break            
            if blank_line_index == 0:
                #print("Issue has no events")
                continue            
            for event_search in range(1, blank_line_index - index):
                issue_array.append(lines[blank_line_index - event_search])
            
            e_index = 0
            prev_etime = 0
            no_labels_flag = 0
            issue_num = line[6:]
            #print(issue_num)
            #print(line[:-1])
            for event in issue_array:
                
                if e_index == 0:
                    o_index = event.find("opened :")
                    e_time = event.find("when :")
                    o_string = event[o_index + 9:event.find(',',o_index)]
                    et_string = event[e_time + 7:event.find(',',e_time)]
                    #print(o_string)
                    #print(et_string)
                    
                    
                    no_label_time[issue_num]= float(et_string) - float(o_string)
                    no_label_time[issue_num] = int(no_label_time[issue_num])
                    #print("Time without any labels: " + str(no_label_time[issue_num])+" seconds")
                    out_string = line[6:-1]+','+str(no_label_time[issue_num])
                    if(no_label_time[issue_num] > 43200):
                        out_string = out_string+',Badsmell (>12 hours)'
                    print(out_string)
                    
                e_index += 1
                    
        index = index + 1 
                
naked_issue()
    