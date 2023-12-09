import re
from math import gcd

input = [line.rstrip() for line in open("day_08\input.txt", "r")]

temp_data = [[re.sub(r'\W+', '', x) for x in line.split()] for line in input[2:]]
input_data = {x[0] : (x[2], x[3]) for x in temp_data}

steps = 0
current_locations = [key for key in input_data if key[-1] == "A"]
steps_for_goal = []
lcm = 1

while len(current_locations) != 0:
    for current_location in current_locations:
        current_locations[current_locations.index(current_location)] = input_data[current_location][0] if list(input[0])[steps % len(input[0])] == "L" else input_data[current_location][1]
    steps += 1
    for location in current_locations:
        if location[-1] == "Z":
            current_locations[current_locations.index(location)] = ""
            steps_for_goal.append(steps)    
    current_locations = [x for x in current_locations if x]

for num in steps_for_goal:
    lcm = lcm * num // gcd(lcm, num)

print(lcm)
    

