with open('input', 'r') as f:
    sum = 0
    for line in f:
        digits = list(filter(str.isdigit, line))
        sum += int(''.join([digits[0],digits[-1]]))
    print(sum)