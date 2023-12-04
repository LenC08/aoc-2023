input = open("day_04\input.txt", "r")

points = 0

for line in input:
    numbers = line.strip().split(" ")[2:]
    numbers = [i for i in numbers if i]
    ind = numbers.index("|")
    winning_numbers = numbers[:ind]
    elves_numbers = numbers[ind + 1:]

    current_pts = 0
    
    for num in winning_numbers:
        if num in elves_numbers:
            if current_pts == 0: current_pts += 1
            else: current_pts *= 2
    points += current_pts
    

print(points)
