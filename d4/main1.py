total = 0
with open('input') as f:
    for line in f:
        winning_numbers = set(int(x) for x in line[10:40].split())
        my_numbers = set(int(x) for x in line[42:117].split())
        total += 2**(len(winning_numbers & my_numbers)-1) if len(winning_numbers & my_numbers) > 0 else 0
print(total)