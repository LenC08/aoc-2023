import re

input = [line.rstrip() for line in open("day_08\input.txt", "r")]

directions = list(input[0])
direction_counter = 0
steps = 0

current_location = "AAA"

while current_location != "ZZZ":
    for i in range(2, len(input)):
        parsed_line = [re.sub(r'\W+', '', x) for x in input[i].split()]
        if parsed_line[0] == current_location:
            current_location = parsed_line[2] if directions[direction_counter] == "L" else parsed_line[3]
            steps += 1
            direction_counter += 1
            if direction_counter == len(directions): direction_counter = 0
            break
print(steps)