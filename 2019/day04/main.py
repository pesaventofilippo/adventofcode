def part1(lines: list[str]) -> int:
    start, end = map(int, lines[0].split("-"))
    count = 0
    for i in range(start, end+1):
        s = str(i)
        if list(s) != sorted(s):
            continue
        if len(set(s)) == len(s):
            continue
        count += 1
    return count


def part2(lines: list[str]) -> int:
    start, end = map(int, lines[0].split("-"))
    count = 0
    for i in range(start, end+1):
        s = str(i)
        if list(s) != sorted(s):
            continue
        if 2 not in [s.count(c) for c in s]:
            continue
        count += 1
    return count


def main():
    with open("input.txt") as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
        print("Part 1:", part1(lines))
        print("Part 2:", part2(lines))


if __name__ == '__main__':
    main()
