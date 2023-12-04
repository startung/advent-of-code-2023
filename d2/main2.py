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
        product = 1
        for count in total_per_game.values():
            product *= count
        print(f"{i+1}={product}")
        sum += product
    print(f"{sum=}")