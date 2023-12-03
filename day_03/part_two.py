input = [line.rstrip() for line in open("day_03\input.txt", "r")]

sum = 0

def get_number_length(line_ind, char_ind):
    extra_right = 0
    extra_left = 0
    while char_ind + extra_right < len(input[line_ind]) - 1 and input[line_ind][char_ind + 1 + extra_right].isdigit():
        extra_right += 1
    while char_ind - extra_left > 0 and input[line_ind][char_ind - 1 - extra_left].isdigit():
        extra_left += 1
    return extra_right + extra_left + 1

def get_and_delete_number(line_ind, char_ind, num_len):
    while char_ind > 0 and input[line_ind][char_ind - 1].isdigit():
        char_ind -= 1
    number = ""
    for i in range(num_len):
        number += input[line_ind][char_ind + i]
        temp = list(input[line_ind])
        temp[char_ind + i] = "."
        input[line_ind] = "".join(temp)
    return int(number)

for line_ind in range(len(input)):
    for char_ind in range(len(input[line_ind])):
        if input[line_ind][char_ind] == "*":
            adjacent_numbers = []
            if line_ind > 0 and input[line_ind - 1][char_ind].isdigit():
                adjacent_numbers.append(get_and_delete_number(line_ind - 1, char_ind, get_number_length(line_ind - 1, char_ind)))
            if line_ind > 0 and char_ind > 0 and input[line_ind - 1][char_ind - 1].isdigit():
                adjacent_numbers.append(get_and_delete_number(line_ind - 1, char_ind - 1, get_number_length(line_ind - 1, char_ind - 1)))
            if line_ind > 0 and char_ind < len(input[line_ind]) - 1 and input[line_ind - 1][char_ind + 1].isdigit():
                adjacent_numbers.append(get_and_delete_number(line_ind - 1, char_ind + 1, get_number_length(line_ind - 1, char_ind + 1)))
            if char_ind > 0 and input[line_ind][char_ind - 1].isdigit():
                adjacent_numbers.append(get_and_delete_number(line_ind, char_ind - 1, get_number_length(line_ind, char_ind - 1)))
            if char_ind < len(input[line_ind]) - 1 and input[line_ind][char_ind + 1].isdigit():
                adjacent_numbers.append(get_and_delete_number(line_ind, char_ind + 1, get_number_length(line_ind, char_ind + 1)))
            if line_ind < len(input) - 1 and input[line_ind + 1][char_ind].isdigit():
                adjacent_numbers.append(get_and_delete_number(line_ind + 1, char_ind, get_number_length(line_ind + 1, char_ind)))
            if line_ind < len(input) - 1 and char_ind > 0 and input[line_ind + 1][char_ind - 1].isdigit():
                adjacent_numbers.append(get_and_delete_number(line_ind + 1, char_ind - 1, get_number_length(line_ind + 1, char_ind - 1)))
            if line_ind < len(input) - 1 and char_ind < len(input[line_ind]) - 1 and input[line_ind + 1][char_ind + 1].isdigit():
                adjacent_numbers.append(get_and_delete_number(line_ind + 1, char_ind + 1, get_number_length(line_ind + 1, char_ind + 1)))
        
            if len(adjacent_numbers) == 2:
                sum += adjacent_numbers[0] * adjacent_numbers[1]



print(sum)