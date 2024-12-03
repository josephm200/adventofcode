# Day 1: Hystorian Hysteria
# 12/1/24

# Part 2 Objective: Find the similarity score calculated by finding common values across the lists.

left_list = []
right_list = []
similarity_score = 0

with open ('input.txt', 'r') as f:
    for line in f:
        line_as_list = line.split()
        left_list.append(int(line_as_list[0]))
        right_list.append(int(line_as_list[1]))
    f.close()

left_list.sort()
right_list.sort()

for i in range(len(left_list)):
    counter = 0
    for j in range(len(right_list)):
        if left_list[i] == right_list[j]:
            counter+=1
    similarity_score+=left_list[i]*counter

print(similarity_score)
