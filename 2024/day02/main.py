def is_safe(levels: list[int]) -> bool:
    is_increasing = all(levels[i] < levels[i + 1] for i in range(len(levels) - 1))
    is_decreasing = all(levels[i] > levels[i + 1] for i in range(len(levels) - 1))
    abs_check = all(1 <= abs(levels[i] - levels[i + 1]) <= 3 for i in range(len(levels) - 1))
    return (is_decreasing or is_increasing) and abs_check


def part1(lines: list[str]) -> int:
    return sum(is_safe([int(x) for x in report.split()]) for report in lines)


def part2(lines: list[str]) -> int:
    total = 0
    for report in lines:
        levels = [int(x) for x in report.split()]
        if is_safe(levels):
            total += 1
        else:
            for i in range(len(levels)):
                new_levels = levels.copy()
                new_levels.pop(i)
                if is_safe(new_levels):
                    total += 1
                    break
    return total


def main():
    with open("input.txt") as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
        print("Part 1:", part1(lines))
        print("Part 2:", part2(lines))


if __name__ == '__main__':
    main()
