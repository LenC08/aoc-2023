import re

input = [line.rstrip() for line in open("day_08\input.txt", "r")]

temp_data = [[re.sub(r'\W+', '', x) for x in line.split()] for line in input[2:]]
input_data = {x[0] : (x[2], x[3]) for x in temp_data}

steps = 0
current_location = "AAA"

while current_location != "ZZZ":  
    current_location = input_data[current_location][0] if list(input[0])[steps % len(input[0])] == "L" else input_data[current_location][1]
    steps += 1

print(steps)