POS = (0, 0)
HEADING = "N"
compass = ["N", "E", "S", "W"]

def left():
    global HEADING
    i = (compass.index(HEADING) - 1) % len(compass)
    HEADING = compass[i]

def right():
    global HEADING
    i = (compass.index(HEADING) + 1) % len(compass)
    HEADING = compass[i]

def step(steps: int):
    global POS
    if HEADING == "N":
        POS = (POS[0], POS[1]+steps)
    elif HEADING == "E":
        POS = (POS[0]+steps, POS[1])
    elif HEADING == "S":
        POS = (POS[0], POS[1]-steps)
    elif HEADING == "W":
        POS = (POS[0]-steps, POS[1])

def part1(lines: list[str]) -> int:
    directions = [(d[0], int(d[1:])) for d in lines[0].split(", ")]
    for heading, steps in directions:
        turn = left if heading == "L" else right
        turn()
        step(steps)
    return abs(POS[0]) + abs(POS[1])

def part2(lines: list[str]) -> int:
    directions = [(d[0], int(d[1:])) for d in lines[0].split(", ")]
    visited = [POS]
    for heading, steps in directions:
        turn = left if heading == "L" else right
        turn()
        for _ in range(steps):
            step(1)
            if POS in visited:
                return abs(POS[0]) + abs(POS[1])
            visited.append(POS)


def main():
    global POS
    with open("input.txt") as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
        POS = (0, 0)
        print("Part 1:", part1(lines))
        POS = (0, 0)
        print("Part 2:", part2(lines))

if __name__ == '__main__':
    main()
