def part1(lines: list[str]) -> int:
    return sum(map(int, lines))


def part2(lines: list[str]) -> int:
    freq = 0
    seen = {freq}
    changes = list(map(int, lines))
    while True:
        for change in changes:
            freq += change
            if freq in seen:
                return freq
            seen.add(freq)


def main():
    with open("input.txt") as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
        print("Part 1:", part1(lines))
        print("Part 2:", part2(lines))


if __name__ == '__main__':
    main()
