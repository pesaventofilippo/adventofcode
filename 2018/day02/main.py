def part1(lines: list[str]) -> int:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    twos = 0
    threes = 0
    for line in lines:
        if any(line.count(c) == 2 for c in alphabet):
            twos += 1
        if any(line.count(c) == 3 for c in alphabet):
            threes += 1
    return twos * threes


def part2(lines: list[str]) -> int:
    for i in range(len(lines)):
        for j in range(i+1, len(lines)):
            diffs = sum(1 for a, b in zip(lines[i], lines[j]) if a != b)
            if diffs == 1:
                common = ''.join(a for a, b in zip(lines[i], lines[j]) if a == b)
                return common


def main():
    with open("input.txt") as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
        print("Part 1:", part1(lines))
        print("Part 2:", part2(lines))


if __name__ == '__main__':
    main()
