file = open("input.txt", "r")
lines = file.read().split("\n")


def turn(left: bool, turns: int, facing: str):
    if not left:
        for _ in range(turns):
            if facing == "N":
                facing = "E"
            elif facing == "E":
                facing = "S"
            elif facing == "S":
                facing = "W"
            elif facing == "W":
                facing = "N"
    else:
        for _ in range(turns):
            if facing == "N":
                facing = "W"
            elif facing == "E":
                facing = "N"
            elif facing == "S":
                facing = "E"
            elif facing == "W":
                facing = "S"
    return facing


pointing = "E" # starting East
pos = [0, 0] # 0 North, 0 East
for inst in lines:
    cmd = inst[0]
    amt = int(inst[1:])

    if cmd == "F":
        cmd = pointing # override direction with "pointing"

    if cmd == "N":
        pos[0] += amt
    elif cmd == "S":
        pos[0] -= amt
    elif cmd == "E":
        pos[1] += amt
    elif cmd == "W":
        pos[1] -= amt
    elif cmd == "L":
        turns = int(amt/90)
        if turns > 0:
            pointing = turn(True, turns, pointing)
        elif turns < 0:
            pointing = turn(False, -turns, pointing)
    elif cmd == "R":
        turns = int(amt/90)
        if turns > 0:
            pointing = turn(False, turns, pointing)
        elif turns < 0:
            pointing = turn(True, -turns, pointing)

print(abs(pos[0]) + abs(pos[1]))
