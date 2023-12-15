from itertools import combinations

def solve(lines: list[str], distance_mult: int) -> int:
    mult_rows: list[int] = []
    mult_cols: list[int] = []
    galaxies: list[tuple[int, int]] = []

    for (i, line) in enumerate(lines):
        row = [c for c in line]
        if all(c == "." for c in row):
            mult_rows.append(i)

    for j in range(len(lines[0])):
        col = [lines[i][j] for i in range(len(lines))]
        if all(c == "." for c in col):
            mult_cols.append(j)

    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == "#":
                galaxies.append((i, j))

    total = 0
    for ((x1, y1), (x2, y2)) in combinations(galaxies, 2):
        passed_rows = sum((min(x1, x2) < ml and max(x1, x2) > ml) for ml in mult_rows)
        passed_cols = sum((min(y1, y2) < ml and max(y1, y2) > ml) for ml in mult_cols)
        total += abs(x2 - x1) + abs(y2 - y1) + (passed_rows + passed_cols) * (distance_mult-1)
    return total

def part1(lines: list[str]) -> int:
    return solve(lines, 2)

def part2(lines: list[str]) -> int:
    return solve(lines, 1000000)


def main():
    with open("input.txt") as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
        print("Part 1:", part1(lines))
        print("Part 2:", part2(lines))


if __name__ == '__main__':
    main()
