def part1(lines: list[str]) -> int:
    precedence_rules: list[tuple[int, int]] = []

    for line in lines:
        if '|' in line:
            a, b = map(int, line.split('|'))
            precedence_rules.append((a, b))
        else:
            updates = map(int, line.split(','))



def part2(lines: list[str]) -> int:
    pass


def main():
    with open("input.txt") as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
        print("Part 1:", part1(lines))
        print("Part 2:", part2(lines))


if __name__ == '__main__':
    main()
