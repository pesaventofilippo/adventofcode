def part1(lines: list[str]) -> int:
    possible = 0
    for line in lines:
        s = [int(x) for x in line.split() if x]
        if (s[0]+s[1] > s[2]) and (s[1]+s[2] > s[0]) and (s[0]+s[2] > s[1]):
            possible += 1
    return possible


def part2(lines: list[str]) -> int:
    possible = 0
    for i in range(0, len(lines)-2, 3):
        s1 = [int(x) for x in lines[i].split() if x]
        s2 = [int(x) for x in lines[i+1].split() if x]
        s3 = [int(x) for x in lines[i+2].split() if x]
        for t in range(3):
            if (s1[t] + s2[t] > s3[t]) and (s2[t] + s3[t] > s1[t]) and (s1[t] + s3[t] > s2[t]):
                possible += 1
    return possible


def main():
    with open("input.txt") as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
        print("Part 1:", part1(lines))
        print("Part 2:", part2(lines))


if __name__ == '__main__':
    main()
