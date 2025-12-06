def part1(lines: list[str]) -> int:
    ranges = [map(int, x.split("-")) for x in lines[0].split(",")]

    def is_invalid(id: int) -> bool:
        s = str(id)
        if len(s) % 2 != 0:
            return False
        return s[:len(s)//2] == s[len(s)//2:]

    total = 0
    for (start, end) in ranges:
        for id in range(start, end+1):
            if is_invalid(id):
                total += id

    return total


def part2(lines: list[str]) -> int:
    ranges = [map(int, x.split("-")) for x in lines[0].split(",")]

    def is_invalid(id: int) -> bool:
        s = str(id)
        for div in range(2, len(s)+1):
            if len(s) % div != 0:
                continue
            if s[:len(s)//div] * div == s:
                return True

        return False

    total = 0
    for (start, end) in ranges:
        for id in range(start, end + 1):
            if is_invalid(id):
                total += id

    return total


def main():
    with open("input.txt") as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
        print("Part 1:", part1(lines))
        print("Part 2:", part2(lines))


if __name__ == '__main__':
    main()
