import re
from math import gcd

input = [line.rstrip() for line in open("day_08\input.txt", "r")]

directions = list(input[0])
direction_counter = 0
steps = 0
current_locations = []
cur_locs_steps = []
lcm = 1

for i in range(2, len(input)):
    if input[i][2] == "A": current_locations.append(input[i][:3]) 

length = len(current_locations)

while length != len(cur_locs_steps):
    for location in current_locations:
        for i in range(2, len(input)):
            parsed_line = [re.sub(r'\W+', '', x) for x in input[i].split()]
            if parsed_line[0] == location:
                current_locations[current_locations.index(location)] = parsed_line[2] if directions[direction_counter] == "L" else parsed_line[3]
                break;
    steps += 1
    direction_counter += 1
    if direction_counter == len(directions): direction_counter = 0

    for location in current_locations:
        if location[-1] == "Z":
            current_locations[current_locations.index(location)] = ""
            cur_locs_steps.append(steps)
    
    current_locations = [x for x in current_locations if x]


for num in cur_locs_steps:
    lcm = lcm*num // gcd(lcm, num)

print(lcm)
    

