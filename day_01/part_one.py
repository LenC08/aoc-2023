input = open("day_one\input.txt", "r")

sum = 0 

def get_first_digit(string):
    for char in string:
        if char.isdigit(): return char

for line in input.readlines():
    cal_value = get_first_digit(line) + get_first_digit(reversed(line))
    sum += int(cal_value)

print(sum)

input.close()

