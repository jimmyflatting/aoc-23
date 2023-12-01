import re

def puzzle_one():
    with open("dec01/input.txt", "r") as file:
        j = file.read().split('\n')

    i = 0
    for k in j:
        n = re.findall(r'\d', k)
        if n:
            x = int(n[0] + n[-1])
            i += x

    print(i)