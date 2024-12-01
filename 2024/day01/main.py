def part1(lines: list[str]) -> int:
    list_a = []
    list_b = []
    for l in lines:
        a, b = l.split()
        list_a.append(int(a))
        list_b.append(int(b))

    list_a = sorted(list_a)
    list_b = sorted(list_b)

    total = 0
    for a, b in zip(list_a, list_b):
        total += abs(a - b)

    return total


def part2(lines: list[str]) -> int:
    list_a = []
    list_b = []
    for l in lines:
        a, b = l.split()
        list_a.append(int(a))
        list_b.append(int(b))

    total = 0
    for a in list_a:
        total += a * list_b.count(a)

    return total


def main():
    with open("input.txt") as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
        print("Part 1:", part1(lines))
        print("Part 2:", part2(lines))


if __name__ == '__main__':
    main()
