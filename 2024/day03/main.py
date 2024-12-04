def part1(lines: list[str]) -> int:
    import re
    instructions = lines[0]
    matches = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', instructions)

    total = 0
    for match in matches:
        a, b = map(int, match)
        total += a * b
    return total


def part2(lines: list[str]) -> int:
    import re
    instructions = lines[0]
    matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", instructions)

    total = 0
    enabled = True
    for match in matches:
        if match == "do()":
            enabled = True
        elif match == "don't()":
            enabled = False
        elif enabled:
            a, b = map(int, match[4:-1].split(","))
            total += a * b
    return total


def main():
    with open("input.txt") as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
        print("Part 1:", part1(lines))
        print("Part 2:", part2(lines))


if __name__ == '__main__':
    main()
