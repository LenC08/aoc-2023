input = open("day_07\input.txt", "r")

sorted_hands = []
total_winnings = 0

all_types = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]

values = {
    "A" : 13,
    "K" : 12,
    "Q" : 11,
    "T" : 10,
    "J" : 1
}

def get_value_if_joker(hand):
    cur_max = 0
    for option in all_types:
        new_hand = hand.replace("J", option, 1)
        if "J" in new_hand:
            pos_max = get_value_if_joker(new_hand)
            cur_max = pos_max if pos_max > cur_max else cur_max
        else:
            pos_max = get_category_value(new_hand)
            cur_max = pos_max if pos_max > cur_max else cur_max
    return cur_max


def get_category_value(hand):
    if hand.count(hand[0]) == 5: return 7
    elif hand.count(hand[0]) == 4 or hand.count(hand[1]) == 4: return 6
    elif len(set(hand)) == 2 and all(hand.count(char) in [2,3] for char in hand): return 5
    elif hand.count(hand[0]) == 3 or  hand.count(hand[1]) == 3 or hand.count(hand[2]) == 3: return 4
    if len(set(hand)) == 3: return 3
    elif len(set(hand)) == 4: return 2
    else: return 1

def insert_hand(hand, value, bid):
    for i in range(len(sorted_hands)):
        if value < sorted_hands[i][1] or (value == sorted_hands[i][1] and is_weaker(hand, sorted_hands[i][0])):
            sorted_hands.insert(i, [hand, value, bid])
            return
    sorted_hands.append([hand, value, bid])

def is_weaker(hand, other_hand):
    for i in range(len(hand)):
        char1 = hand[i] if hand[i].isdigit() else values[hand[i]]
        char2 = other_hand[i] if other_hand[i].isdigit() else values[other_hand[i]]
        if int(char1) < int(char2):
            return True
        elif int(char2) < int(char1):
            return False
    return False

for line in input:
    hand, bid = line.strip().split()[0], int(line.strip().split()[1])
    if "J" in hand:
        category_value = get_value_if_joker(hand)
    else: category_value = get_category_value(hand)
    insert_hand(hand, category_value, bid)

for i in range(len(sorted_hands)):
    total_winnings += sorted_hands[i][2] * (i + 1)

print(total_winnings)