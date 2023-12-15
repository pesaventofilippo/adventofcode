from functools import cache

@cache
def solve(springs: str, check: tuple[int]) -> int:
    if not check:
        return 0 if "#" in springs else 1
    if not springs:
        return 0

    nextc = springs[0]
    run_length = check[0]
    total = 0
    if nextc in ".?":
        total += solve(springs[1:], check)
    if nextc in "#?":
        this_group = springs[:run_length].replace("?", "#")
        if len(this_group) == run_length and this_group.count('#') == run_length:
            if len(springs) == run_length:
                total += 1 if len(check) == 1 else 0
            elif springs[run_length] in ".?":
                total += solve(springs[run_length+1:], check[1:])

    return total


def part1(lines: list[str]) -> int:
    total = 0
    for line in lines:
        springs, check = line.split(" ")
        check = tuple(int(x) for x in check.split(","))
        total += solve(springs, check)
    return total


def part2(lines: list[str]) -> int:
    total = 0
    for line in lines:
        springs, check = line.split(" ")
        springs = '?'.join([springs]*5)
        check = tuple(map(int, check.split(",")))*5
        total += solve(springs, check)
    return total


def main():
    with open("input.txt") as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
        print("Part 1:", part1(lines))
        print("Part 2:", part2(lines))


if __name__ == '__main__':
    main()
