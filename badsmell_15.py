import string, os, sys

def quick_labels():
    f=open("Data_Output.txt", "r")
    lines = f.readlines()
    index = 0
    quick_labels = {}
    print('Issue,Label,Time Label is open (seconds)')
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
            for event in issue_array:
                a_index = event.find("action :")
                l_index = event.find("what :")
                e_time = event.find("when :")
                #print(event)
                a_string = event[a_index + 9:event.find(',',a_index)]
                l_string = event[l_index + 7:event.find(',',l_index)]                
                et_string = event[e_time + 7:event.find(',',e_time)]
                if ((e_index + 1 < len(issue_array)) and a_string == "labeled"):
                    for next_e in range(e_index+1, len(issue_array)):
                        #print("   "+issue_array[next_e])
                        a_index = issue_array[next_e].find("action :")
                        l_index = issue_array[next_e].find("what :")
                        e_time = issue_array[next_e].find("when :")
                        na_string = issue_array[next_e][a_index + 9:issue_array[next_e].find(',',a_index)]
                        nl_string = issue_array[next_e][l_index + 7:issue_array[next_e].find(',',l_index)]
                        net_string = issue_array[next_e][e_time + 7:issue_array[next_e].find(',',e_time)]
                        #print(l_string+":"+nl_string)
                        if (l_string == nl_string and na_string == "unlabeled"):
                            #print("found match")
                            diff = float(net_string) - float(et_string) 
                            diff = int(diff)
                            out_string = line[6:-1]+','+l_string+','+str(diff)
                            if diff < 300:
                                out_string = out_string+',Badsmell'
                            print(out_string)
                e_index += 1
                
        index = index + 1 
                
quick_labels()