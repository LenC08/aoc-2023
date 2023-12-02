input = open("day_02\input.txt", "r")

sum = 0

contents = {
    "red" : 12,
    "green" : 13,
    "blue" : 14
}

for line in input:
    line = line.split(" ")
    id = int("".join([i for i in line[1] if i.isdigit()]))
    line = line[2:]

    possible = True
    for i in range(0, len(line), 2) :
        if int(line[i]) > contents[line[i + 1].strip(",;\n")]:
            possible = False
            break
    
    if possible:
        sum += id

print(sum)