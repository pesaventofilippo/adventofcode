def first(lines):
    incs = 0
    for i in range(1, len(lines)):
        if lines[i] > lines[i - 1]:
            incs += 1
    return incs


def second(lines):
    incs = 0
    last = max(lines)
    for i in range(len(lines) - 2):
        try:
            win = sum(lines[i:i+3])
            if win > last:
                incs += 1
            last = win
        except IndexError:
            pass
    return incs


with open("input.txt") as f:
    lines = [int(x) for x in f.readlines()]
    print(first(lines))
    print(second(lines))
