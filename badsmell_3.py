import string, os, sys

def naked_issue():
    f=open("Data_Output.txt", "r")
    lines = f.readlines()
    index = 0
    no_label_time = {}
    
    for line in lines: 
        if line.startswith("ISSUE"): 
            blank_line_index = 0
            issue_array = []
            for blank_search in range(i+1, len(lines)):
                if lines[blank_search].strip == '':
                    blank_line_index = blank_search
                    break
            if blank_line_index == 0:
                print("Issue has no events")
                continue
            for event_search in range(1, blank_line_index - index - 1):
                issue_array.append(lines[blank_line_index - event_search])
    