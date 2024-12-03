# Day 2: Red-Nosed Reports
# 12/2/24

# Part 1 Objective: Identiy safe reports (lines of input file that are all increasing/decreasing or differ by 1 <= x <= 3)

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

with open ("input.txt", "r") as input_file:
    for line in input_file:
        levels = list(map(int, line.split())) # convert list of strings to ints
        
        if ((is_ascending(levels) == True or is_descending(levels) == True) and is_in_range(levels) == True):
            safe_counter+=1
    print(safe_counter)

