input = open("day_02\input.txt", "r")

sum = 0

for line in input:

    contents = dict(red=0, green=0, blue=0)
    
    line = line.split(" ")
    id = int("".join([i for i in line[1] if i.isdigit()]))
    line = line[2:]

    for i in range(0, len(line), 2) :
        line[i + 1] = line[i + 1].strip(",;\n")
        if int(line[i]) > contents[line[i + 1]]:
            contents[line[i + 1]] = int(line[i])
    sum += contents["red"] * contents["green"] * contents["blue"]

print(sum)