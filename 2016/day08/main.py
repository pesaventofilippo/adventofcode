def rprint(screen: list[list[bool]]):
    for i in range(len(screen)):
        for j in range(len(screen[0])):
            print('#' if screen[i][j] else ' ', end="")
        print()

def rect(screen: list[list[bool]], a: int, b: int):
    for j in range(a):
        for i in range(b):
            screen[i][j] = True

def rotate_row(screen: list[list[bool]], a: int, b: int):
    for _ in range(b):
        screen[a] = [screen[a][-1]] + screen[a][:-1]

def rotate_col(screen: list[list[bool]], a: int, b: int):
    for _ in range(b):
        last = screen[-1][a]
        for i in range(len(screen)-1, 0, -1):
            screen[i][a] = screen[i-1][a]
        screen[0][a] = last


def part1(lines: list[str]) -> int:
    SCREEN = []
    for _ in range(6):
        SCREEN.append([False] * 50)

    for instruction in lines:
        if instruction.startswith("rect "):
            a, b = instruction.split(" ")[1].split("x")
            rect(SCREEN, int(a), int(b))
        elif instruction.startswith("rotate row "):
            raw = instruction.split(" ")
            a = int(raw[2][2:])
            b = int(raw[4])
            rotate_row(SCREEN, a, b)
        elif instruction.startswith("rotate column "):
            raw = instruction.split(" ")
            a = int(raw[2][2:])
            b = int(raw[4])
            rotate_col(SCREEN, a, b)

    total = 0
    for i in range(len(SCREEN)):
        for j in range(len(SCREEN[0])):
            total += SCREEN[i][j]
    return total


def part2(lines: list[str]) -> int:
    SCREEN = []
    for _ in range(6):
        SCREEN.append([False] * 50)

    for instruction in lines:
        if instruction.startswith("rect "):
            a, b = instruction.split(" ")[1].split("x")
            rect(SCREEN, int(a), int(b))
        elif instruction.startswith("rotate row "):
            raw = instruction.split(" ")
            a = int(raw[2][2:])
            b = int(raw[4])
            rotate_row(SCREEN, a, b)
        elif instruction.startswith("rotate column "):
            raw = instruction.split(" ")
            a = int(raw[2][2:])
            b = int(raw[4])
            rotate_col(SCREEN, a, b)

    rprint(SCREEN)


def main():
    with open("input.txt") as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
        print("Part 1:", part1(lines))
        print("Part 2:", part2(lines))


if __name__ == '__main__':
    main()
