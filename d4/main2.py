with open('input') as f:
    input = f.readlines()

cards = [1] * len(input)

for idx, line in enumerate(input):
    winning_numbers = set(int(x) for x in line[10:40].split())
    my_numbers = set(int(x) for x in line[42:117].split())
    for jdx in range(len(winning_numbers & my_numbers)):
        cards[idx + jdx + 1] += cards[idx]

print(sum(cards))

