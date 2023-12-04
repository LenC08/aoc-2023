input = open("day_04\input.txt", "r")

total_cards = 0

amount_dict = dict()

card_num = 0

for line in input:
    
    card_num += 1

    if card_num in amount_dict:
        amount_dict[card_num] += 1
    else:
        amount_dict[card_num] = 1
    
    numbers = line.strip().split(" ")[2:]
    numbers = [i for i in numbers if i]
    ind = numbers.index("|")
    winning_numbers = numbers[:ind]
    elves_numbers = numbers[ind + 1:]

    match_amount = 0
    
    for num in winning_numbers:
        if num in elves_numbers:
            match_amount += 1
    
    for i in range(1, match_amount + 1):
        if card_num + i in amount_dict:
            amount_dict[card_num + i] += amount_dict[card_num]
        else:
            amount_dict[card_num + i] = amount_dict[card_num]
    

total_cards = sum(amount_dict.values())

    

print(total_cards)
