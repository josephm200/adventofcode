# Day 2: Red-Nosed Reports
# 12/2/24

# Part 2 Objective: Allow for one error in safe reports.

safe_counter = 0

def is_ascending(list):
    for i in range(len(list) - 1):
        if list[i] > list[i+1]:
            return False
    return True
    
def is_descending(list):
    for i in range(len(list) - 1):
        if list[i] < list[i+1]:
            return False
    return True
    
def is_in_range(list):
    for i in range(len(list) - 1):
        if abs(list[i] - list[i+1]) < 1 or abs(list[i] - list[i+1]) > 3:
            return False
    return True

def check_removal(list):
    if ((is_ascending(list) == True or is_descending(list) == True) and is_in_range(list) == True):
        return True
    for i in range(len(list)):
        temp_list = list[:i] + list[i+1:] # removes ith element
        if ((is_ascending(temp_list) == True or is_descending(temp_list) == True) and is_in_range(temp_list) == True):
            return True
    return False
        
with open ("input.txt", "r") as input_file:
    for line in input_file:
        levels = list(map(int, line.split())) # convert list of strings to ints
        
        if check_removal(levels):
            safe_counter+=1
    print(safe_counter)

