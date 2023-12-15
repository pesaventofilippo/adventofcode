def part1(lines: list[str]) -> str:
    res = ""
    for j in range(len(lines[0])):
        col = [row[j] for row in lines]
        count = {c: col.count(c) for c in col}
        res += max(count, key=count.get)
    return res


def part2(lines: list[str]) -> int:
    res = ""
    for j in range(len(lines[0])):
        col = [row[j] for row in lines]
        count = {c: col.count(c) for c in col}
        res += min(count, key=count.get)
    return res


def main():
    with open("input.txt") as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
        print("Part 1:", part1(lines))
        print("Part 2:", part2(lines))


if __name__ == '__main__':
    main()
