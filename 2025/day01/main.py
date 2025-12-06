def part1(lines: list[str]) -> int:
    dial = 50
    total = 0
    for line in lines:
        amt = int(line.replace("L", "-").replace("R", ""))
        dial = (dial + amt) % 100
        if dial == 0:
            total += 1
    return total


def part2(lines: list[str]) -> int:
    dial = 50
    total = 0
    for line in lines:
        amt = int(line.replace("L", "-").replace("R", ""))
        for _ in range(abs(amt)):
            dial = (dial + (1 if amt > 0 else -1)) % 100
            if dial == 0:
                total += 1
    return total


def main():
    with open("input.txt") as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
        print("Part 1:", part1(lines))
        print("Part 2:", part2(lines))


if __name__ == '__main__':
    main()
