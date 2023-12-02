input = open("day_one\input.txt", "r")

sum = 0

number_array = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def get_first_digit(string, backwards):    
    string = replace_numbers(string, backwards)  

    if backwards:
        string = reversed(string) 
    for char in string:
        if char.isdigit(): return char


def replace_numbers(string, backwards): 
    if backwards:
        i = len(string)
        while i > 0:
            for number in number_array:
                if number in string[i:]:
                    string = string.replace(number, str(number_array.index(number) + 1))
            i -= 1
    else: 
        for i in range(len(string)):
            for number in number_array:
                if number in string[:i]:
                    string = string.replace(number, str(number_array.index(number) + 1))
    
    return string
        

for line in input.readlines():    
    cal_value = get_first_digit(line, 0) + get_first_digit(line, 1)
    sum += int(cal_value)

print(sum)

input.close()

