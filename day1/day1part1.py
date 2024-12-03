# Day 1: Hystorian Hysteria
# 12/1/24

# Part 1 Objective: Find the minimum distance between the ordered pairs of points across two different lists.

left_list = []
right_list = []
diff = 0

with open ('input.txt', 'r') as f:
    for line in f:
        line_as_list = line.split()
        left_list.append(int(line_as_list[0]))
        right_list.append(int(line_as_list[1]))
    f.close()

left_list.sort()
right_list.sort()

for i in range(len(left_list)):
    diff += abs(left_list[i] - right_list[i])

print(diff)
