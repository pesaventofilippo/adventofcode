SIZE = 1000

def part1(lines: list[str]) -> int:
    grid = [[0] * SIZE for _ in range(SIZE)]
    for claim in lines:
        id, _, coords, size = claim.split(" ")
        id = int(id[1:])
        x, y = map(int, coords[:-1].split(","))
        w, h = map(int, size.split("x"))
        for i in range(x, x + w):
            for j in range(y, y + h):
                grid[i][j] += 1

    return sum(1 for i in range(SIZE) for j in range(SIZE) if grid[i][j] > 1)


def part2(lines: list[str]) -> int:
    grid = [[0] * SIZE for _ in range(SIZE)]
    for claim in lines:
        id, _, coords, size = claim.split(" ")
        id = int(id[1:])
        x, y = map(int, coords[:-1].split(","))
        w, h = map(int, size.split("x"))
        for i in range(x, x + w):
            for j in range(y, y + h):
                grid[i][j] = id if grid[i][j] == 0 else -1

    for claim in lines:
        id, _, coords, size = claim.split(" ")
        id = int(id[1:])
        x, y = map(int, coords[:-1].split(","))
        w, h = map(int, size.split("x"))
        intact = True
        for i in range(x, x + w):
            for j in range(y, y + h):
                if grid[i][j] != id:
                    intact = False
                    break
            if not intact:
                break
        if intact:
            return id


def main():
    with open("input.txt") as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
        print("Part 1:", part1(lines))
        print("Part 2:", part2(lines))


if __name__ == '__main__':
    main()
