def first(input):
    x = 0
    z = 0
    for c, d in input:
        if c == "forward":
            x += d
        elif c == "up":
            z -= d
        elif c == "down":
            z += d
    return x * z


def second(input):
    x = 0
    z = 0
    aim = 0
    for c, d in input:
        if c == "forward":
            x += d
            z += aim * d
        elif c == "up":
            aim -= d
        elif c == "down":
            aim += d
    return x * z


with open("input.txt") as f:
    instr = [(c, int(d)) for c, d in [line.split() for line in f.readlines()]]
    print(first(instr))
    print(second(instr))
