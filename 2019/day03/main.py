def part1(lines: list[str]) -> int:
    cable1 = lines[0].split(",")
    cable2 = lines[1].split(",")

    points1 = set()
    x, y = 0, 0
    for move in cable1:
        direction = move[0]
        length = int(move[1:])
        for _ in range(length):
            if direction == "U":
                y += 1
            elif direction == "D":
                y -= 1
            elif direction == "R":
                x += 1
            elif direction == "L":
                x -= 1
            points1.add((x, y))

    points2 = set()
    x, y = 0, 0
    for move in cable2:
        direction = move[0]
        length = int(move[1:])
        for _ in range(length):
            if direction == "U":
                y += 1
            elif direction == "D":
                y -= 1
            elif direction == "R":
                x += 1
            elif direction == "L":
                x -= 1
            points2.add((x, y))

    intersections = points1.intersection(points2) - {(0, 0)}
    return min(abs(x) + abs(y) for x, y in intersections)


def part2(lines: list[str]) -> int:
    cable1 = lines[0].split(",")
    cable2 = lines[1].split(",")

    points1 = set()
    visits1 = dict()
    x, y, s = 0, 0, 0
    for move in cable1:
        direction = move[0]
        length = int(move[1:])
        for _ in range(length):
            if direction == "U":
                y += 1
            elif direction == "D":
                y -= 1
            elif direction == "R":
                x += 1
            elif direction == "L":
                x -= 1
            s += 1
            points1.add((x, y))
            if (x, y) not in visits1:
                visits1[(x, y)] = s

    points2 = set()
    visits2 = dict()
    x, y, s = 0, 0, 0
    for move in cable2:
        direction = move[0]
        length = int(move[1:])
        for _ in range(length):
            if direction == "U":
                y += 1
            elif direction == "D":
                y -= 1
            elif direction == "R":
                x += 1
            elif direction == "L":
                x -= 1
            s += 1
            points2.add((x, y))
            if (x, y) not in visits2:
                visits2[(x, y)] = s

    intersections = points1.intersection(points2) - {(0, 0)}
    return min(visits1[(x,y)] + visits2[(x,y)] for x, y in intersections)


def main():
    with open("input.txt") as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
        print("Part 1:", part1(lines))
        print("Part 2:", part2(lines))


if __name__ == '__main__':
    main()
