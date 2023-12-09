input = open("day_09\input.txt", "r")

result = 0

for line in input:
    sequences = [[int(x) for x in line.strip().split()]]
    while len(set(sequences[-1])) != 1:
        new_sequence = []
        for i in range(len(sequences[-1]) - 1):
            new_sequence.append(sequences[-1][i + 1] - sequences[-1][i])
        sequences.append(new_sequence)
    
    result += sum([seq[-1] for seq in sequences])

print(result)


    
