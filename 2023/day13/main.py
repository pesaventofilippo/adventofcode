from itertools import groupby

def check_row_reflection(pattern: list[str], index: int) -> bool:
    rows_before = reversed(pattern[:index])
    rows_after = pattern[index:]
    return all(r1 == r2 for (r1, r2) in zip(rows_before, rows_after))


def check_almost_reflection(pattern: list[str], index: int) -> bool:
    rows_before = reversed(pattern[:index])
    rows_after = pattern[index:]
    diffs = 0
    for r1, r2 in zip(rows_before, rows_after):
        if r1 != r2:
            diffs += sum(c1 != c2 for c1, c2 in zip(r1, r2))
    return diffs == 1


def transpose(pattern: list[str]) -> list[str]:
    transposed = []
    for j in range(len(pattern[0])):
        transposed.append(''.join(row[j] for row in pattern))
    return transposed


def part1(lines: list[str]) -> int:
    total = 0
    patterns = [list(group) for k, group in groupby(lines, bool) if k]
    for pattern in patterns:
        total += 100 * sum(i for i in range(1, len(pattern)) if check_row_reflection(pattern, i))
        transposed = transpose(pattern)
        total += sum(i for i in range(1, len(transposed)) if check_row_reflection(transposed, i))
    return total


def part2(lines: list[str]) -> int:
    total = 0
    patterns = [list(group) for k, group in groupby(lines, bool) if k]
    for pattern in patterns:
        total += 100 * sum(i for i in range(1, len(pattern)) if check_almost_reflection(pattern, i))
        transposed = transpose(pattern)
        total += sum(i for i in range(1, len(transposed)) if check_almost_reflection(transposed, i))
    return total


def main():
    with open("input.txt") as f:
        lines = [l.strip() for l in f.readlines()]
        print("Part 1:", part1(lines))
        print("Part 2:", part2(lines))


if __name__ == '__main__':
    main()
