input = open("day_07\input.txt", "r")

sorted_hands = []
total_winnings = 0

values = {
    "A" : 14,
    "K" : 13,
    "Q" : 12,
    "J" : 11,
    "T" : 10
}

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
    category_value = get_category_value(hand)
    insert_hand(hand, category_value, bid)

for i in range(len(sorted_hands)):
    total_winnings += sorted_hands[i][2] * (i + 1)

print(total_winnings)