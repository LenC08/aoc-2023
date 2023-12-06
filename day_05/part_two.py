input = [line.rstrip() for line in open("day_05\input.txt", "r")]

seeds = []
new_ranges = []

input_nums = [int(x) for x in input[0].strip().split()[1:]]
for i in range(0, len(input_nums), 2):
    seeds.append([input_nums[i], input_nums[i] + input_nums[i + 1] - 1])

for line in input:
    if line == "":
        seeds += new_ranges
        new_ranges = []
    elif not line[0].isdigit():
        pass
    else:
        line = [int(x) for x in line.strip().split()]
        for seed in seeds:
            if seed[0] > line[1] + line[2] - 1 or seed[1] < line[1]:
                pass
            elif seed[1] >= line[1] and seed[1] <= line[1] + line[2] - 1:
                if seed[0] >= line[1]:
                    new_ranges.append([line[0] + seed[0] - line[1], line[0] + seed[1] - line[1]])
                    seeds[seeds.index(seed)] = ""
                else:
                    new_ranges.append([line[0], line[0] + seed[1] - line[1]])
                    seed[1] = line[1] - 1
            elif seed[0] <= line[1] + line[2] - 1 and seed[0] >= line[0]:
                if seed[1] <= line[1] + line[2] - 1:
                    new_ranges.append([line[0] + seed[0] - line[1], line[0] + seed[1] - line[1]])
                    seeds[seeds.index(seed)] = ""
                else:
                    new_ranges.append([line[0] + seed[0] - line[1], line[0] + line[2] - 1])
                    seed[0] = line[1] + line[2]

        seeds = [i for i in seeds if i]

seeds += new_ranges

lowest = seeds[0][0]
for seed in seeds:
    if seed[0] < lowest:
        lowest = seed[0]
print(lowest)