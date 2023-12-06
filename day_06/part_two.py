input = [line.rstrip() for line in open("day_06\input.txt", "r")]

time = int("".join(input[0].strip().split()[1:]))
distance = int("".join(input[1].strip().split()[1:]))

result = 0

number_of_ways = 0
for j in range(time):
    if j * (time - j) > distance:
        number_of_ways += 1

if result == 0: result += number_of_ways
else: result *= number_of_ways

print(result)