import string, os, sys

def table_gen():
    f=open("Data_Output_m.txt", "r")
    lines = f.readlines()
    index = 0
    no_label_time = {}
    print('Issue #,Issue Opened Time (s),Issue Closed Time (s),Issue Total Alive Time (s),Label Name,Label Action,Event Time (s),Update Time (s),User Name,Num of Comments,Milestone Name,Milestone Created Time (s),Milestone Closed Time (s),Milestone Due Date (s),Milestone Total Issues')
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
            
            
            for event in issue_array:                 
                out_string = line[6:-1]
                opened_index = event.find("opened :")
                opened_string = event[opened_index + 9:event.find(',',opened_index)]
                out_string += ','+opened_string
                
                ended_index = event.find("ended :")
                ended_string = event[ended_index + 8:event.find(',',ended_index)]
                out_string += ','+ended_string
                
                alive_index = event.find("alive :")
                alive_string = event[alive_index + 8:event.find(',',alive_index)]                
                out_string += ','+alive_string
                
                what_index = event.find("what :")
                what_string = event[what_index + 7:event.find(',',what_index)]
                out_string += ','+what_string
                
                action_index = event.find("action :")
                action_string = event[action_index + 9:event.find(',',action_index)]
                out_string += ','+action_string
                
                when_index = event.find("when :")
                when_string = event[when_index + 7:event.find(',',when_index)]
                out_string += ','+when_string
                
                updated_index = event.find("updated :")
                updated_string = event[updated_index + 10:event.find(',',updated_index)]
                out_string += ','+updated_string
                
                user_index = event.find("user :")
                user_string = event[user_index + 7:event.find(',',user_index)]
                out_string += ','+user_string
                
                comments_index = event.find("comments :")
                comments_index_string = event[comments_index + 11:event.find(',',comments_index)]                
                out_string += ','+comments_index_string
                
                mname_index = event.find("milestone_name :")
                mname_string = event[mname_index + 17:event.find(',',mname_index)]
                out_string += ','+mname_string
                
                mcreated_index = event.find("milestone_created :")
                mcreated_string = event[mcreated_index + 20:event.find(',',mcreated_index)]
                out_string += ','+mcreated_string
                
                mclosed_index = event.find("milestone_closed :")
                mclosed_string = event[mclosed_index + 19:event.find(',',mclosed_index)]
                out_string += ','+mclosed_string
                
                mdue_index = event.find("milestone_due :")
                mdue_string = event[mdue_index + 16:event.find(',',mdue_index)]
                out_string += ','+mdue_string
                
                mtotal_index = event.find("milestone_total :")
                mtotal_string = event[mtotal_index + 18:event.find(',',mtotal_index)]
                out_string += ','+mtotal_string
                
                print(out_string)
                                               
                
                
                    
                         
        index = index + 1 
                
table_gen()