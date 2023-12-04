OKGREEN = '\033[92m'
END = '\033[0m'

# 12 red cubes, 13 green cubes, and 14 blue cubes
target = {'red': 12, 'green': 13, 'blue': 14}

with open("input", "r") as f:
    sum = 0
    for i, line in enumerate(f.readlines()):
        draws = line[:-1].split(": ")[1].split("; ")
        total_per_game = {}
        for draw in draws:
            colours = draw.split(", ")
            for totals in colours:
                count, colour = totals.split(" ")
                if colour in total_per_game:
                    total_per_game[colour] = max(total_per_game[colour], int(count))
                else:
                    total_per_game[colour] = int(count)
        if all(total_per_game[colour] <= target[colour] for colour in target):
            print(OKGREEN, i+1, total_per_game, END)
            sum += i+1
        else:
            print("", i+1, total_per_game)
    print(sum)