NORTH = (-1, 0)
EAST = (0, 1)
SOUTH = (1, 0)
WEST = (0, -1)

neighboursMap: dict[str, tuple[tuple[int, int]]] = {
    '|': (NORTH, SOUTH),
    '-': (EAST, WEST),
    'L': (NORTH, EAST),
    'J': (NORTH, WEST),
    '7': (SOUTH, WEST),
    'F': (SOUTH, EAST)
}

def pipeAt(lines: list[str], x: int, y: int) -> str:
    if (x < 0) or (y < 0) or (x > len(lines)) or (y > len(lines[0])):
        return None
    return lines[x][y]

def neighbours(lines: list[str], x: int, y: int) -> list[tuple[int, int]]:
    pipe = pipeAt(lines, x, y)
    if not pipe:
        return None

    if pipe == 'S':
        neigh = []
        for dir in (NORTH, EAST, SOUTH, WEST):
            if (p := pipeAt(lines, x+dir[0], y+dir[1])) is not None:
                if (dir == NORTH and p in "|7F") or (dir == SOUTH and p in "|LJ") \
                    or (dir == EAST and p in "-J7") or (dir == WEST and p in "-LF"):
                    neigh.append((x+dir[0], y+dir[1]))
        return neigh

    if pipe not in neighboursMap:
        return None

    return [(x+n[0], y+n[1]) for n in neighboursMap[pipe]]


def part1(lines: list[str]) -> int:
    startPoint = None
    for i, line in enumerate(lines):
        if 'S' in line:
            startPoint = (i, line.index('S'))

    loop = []
    curNode = startPoint
    while curNode not in loop:
        loop.append(curNode)
        neigh = neighbours(lines, *curNode)
        curNode = neigh[0] if neigh[0] not in loop else neigh[1]

    return len(loop) // 2


def part2(lines: list[str]) -> int:
    startPoint = None
    for i, line in enumerate(lines):
        if 'S' in line:
            startPoint = (i, line.index('S'))

    loop = []
    curNode = startPoint
    while curNode not in loop:
        loop.append(curNode)
        neigh = neighbours(lines, *curNode)
        curNode = neigh[0] if neigh[0] not in loop else neigh[1]

    full_dim = len(lines)
    inside_dim = full_dim // 4
    center = full_dim // 2

    # Trick from visualization: all points inside the loop are enclosed in a square a quarter of the size
    # of the full square. Inside this square, points are either part of the loop, or inside the loop. Neat!
    inside_count = 0
    for i in range(center-inside_dim, center+inside_dim+1):
        for j in range(center-inside_dim, center+inside_dim+1):
            if (i, j) not in loop:
                inside_count += 1
    return inside_count


def main():
    with open("input.txt") as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
        print("Part 1:", part1(lines))
        print("Part 2:", part2(lines))


if __name__ == '__main__':
    main()
