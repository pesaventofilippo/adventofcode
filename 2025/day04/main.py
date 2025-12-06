def part1(lines: list[str]) -> int:
    grid = [[x for x in line] for line in lines]

    def neighs(x: int, y: int) -> int:
        total = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[nx]) and grid[nx][ny] == '@':
                    total += 1
        return total

    count = 0
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == '@' and neighs(x, y) < 4:
                count += 1
    return count


def part2(lines: list[str]) -> int:
    grid = [[x for x in line] for line in lines]

    def neighs(x: int, y: int) -> int:
        total = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[nx]) and grid[nx][ny] == '@':
                    total += 1
        return total

    count = 0
    recheck = True
    while recheck:
        recheck = False
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == '@' and neighs(x, y) < 4:
                    count += 1
                    grid[x][y] = '.'
                    recheck = True
    return count


def main():
    with open("input.txt") as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
        print("Part 1:", part1(lines))
        print("Part 2:", part2(lines))


if __name__ == '__main__':
    main()
