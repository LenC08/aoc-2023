input = [line.rstrip() for line in open("day_05\input.txt", "r")]

seeds = []

for i in [int(x) for x in input[0].strip().split()[1:]]:
    seeds.append([i, False])
    input.pop(0)

for line in input:
    if line == "":
        for i in range(len(seeds)):
            seeds[i][1] = False
    elif not line[0].isdigit():
        pass
    else:
        line = [int(x) for x in line.strip().split()]
        for seed in seeds:
            if seed[1] is False and line[1] <= seed[0] <= line[1] + line[2] - 1:
                seed[0] = line[0] + seed[0] - line[1]
                seed[1] = True


lowest = seeds[0][0]
for seed in seeds:
    if seed[0] < lowest:
        lowest = seed[0]
    

print(lowest)