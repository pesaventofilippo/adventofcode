file = open("input.txt", "r")
lines = file.read().split("\n")

def turn(left: bool, turns: int, pos: list):
    wp = pos.copy()
    if left:
        for _ in range(turns):
            wp = [wp[1], -wp[0]]
    else:
        for _ in range(turns):
            wp = [-wp[1], wp[0]]
    return wp


wpos = [1, 10]
spos = [0, 0]
for inst in lines:
    cmd = inst[0]
    amt = int(inst[1:])

    if cmd == "F":
        spos[0] += wpos[0] * amt
        spos[1] += wpos[1] * amt

    if cmd == "N":
        wpos[0] += amt
    elif cmd == "S":
        wpos[0] -= amt
    elif cmd == "E":
        wpos[1] += amt
    elif cmd == "W":
        wpos[1] -= amt

    elif cmd == "L":
        turns = int(amt/90)
        if turns > 0:
            wpos = turn(True, turns, wpos)
        elif turns < 0:
            wpos = turn(False, -turns, wpos)
    elif cmd == "R":
        turns = int(amt/90)
        if turns > 0:
            wpos = turn(False, turns, wpos)
        elif turns < 0:
            wpos = turn(True, -turns, wpos)

print(abs(spos[0]) + abs(spos[1]))
