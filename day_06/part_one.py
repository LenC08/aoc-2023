input = [line.rstrip() for line in open("day_06\input.txt", "r")]

time_values = [int(x) for x in input[0].strip().split()[1:]]
distance_values = [int(x) for x in input[1].strip().split()[1:]]

result = 0

for i in range(len(time_values)):
    number_of_ways = 0
    for j in range(time_values[i]):
        if j * (time_values[i] - j) > distance_values[i]:
            number_of_ways += 1
    
    if result == 0: result += number_of_ways
    else: result *= number_of_ways

print(result)