input = open("day_09\input.txt", "r")

result = 0

for line in input:
    sequences = [[int(x) for x in line.strip().split()]]
    while len(set(sequences[0])) != 1:
        new_sequence = []
        for i in range(len(sequences[0]) - 1):
            new_sequence.append(sequences[0][i + 1] - sequences[0][i])
        sequences.insert(0, new_sequence)
    
    prev_val = sequences[0][0]
    for i in range(len(sequences) - 1):
        prev_val = sequences[i + 1][0] - prev_val
        
    result += prev_val

print(result)


    
