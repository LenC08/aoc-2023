input = [line.rstrip() for line in open("day_03\input.txt", "r")]

sum = 0

def get_number_length(line_ind, char_ind):
    length = 1
    while char_ind + length - 1 < len(input[line_ind]) - 1 and input[line_ind][char_ind + length].isdigit():
        length += 1
    return length

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
        if input[line_ind][char_ind].isdigit():
            valid = False
            length = get_number_length(line_ind, char_ind)
            for i in range(length):
                if not line_ind == 0 and not input[line_ind - 1][char_ind + i].isdigit() and not input[line_ind - 1][char_ind + i] == ".":
                    valid = True
                    break
                if not line_ind == 0 and not char_ind + i == 0 and not input[line_ind - 1][char_ind + i - 1].isdigit() and not input[line_ind - 1][char_ind - 1] == ".":
                    valid = True
                    break
                if not line_ind == 0 and not char_ind + i == len(input[line_ind]) - 1 and not input[line_ind - 1][char_ind + i + 1].isdigit() and not input[line_ind - 1][char_ind + i + 1] == ".":
                    valid = True
                    break
                if not char_ind + i == 0 and not input[line_ind][char_ind + i - 1].isdigit() and not input[line_ind][char_ind + i - 1] == ".":
                    valid = True
                    break
                if not char_ind + i == len(input[line_ind]) - 1 and not input[line_ind][char_ind + i + 1].isdigit() and not input[line_ind][char_ind + i + 1] == ".":
                    valid = True
                    break
                if not line_ind == len(input) - 1 and not input[line_ind + 1][char_ind + i].isdigit() and not input[line_ind + 1][char_ind + i]== ".":
                    valid = True
                    break
                if not line_ind == len(input) - 1 and not char_ind + i == 0 and not  input[line_ind + 1][char_ind + i - 1].isdigit() and not input[line_ind + 1][char_ind + i - 1] == ".":
                    valid = True
                    break
                if not line_ind == len(input) - 1 and not char_ind + i == len(input[line_ind]) - 1 and not  input[line_ind + 1][char_ind + i + 1].isdigit() and not input[line_ind + 1][char_ind + i + 1] == ".":
                    valid = True
                    break
            
            if valid:
                sum += get_and_delete_number(line_ind, char_ind, length)

print(sum)