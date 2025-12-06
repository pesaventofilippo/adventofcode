def maxn(bank: list[int], n: int) -> int:
    if n == 1:
        return max(bank)
    total = max(bank[:-n+1])
    idx = bank.index(total)
    total *= 10 ** (n - 1)
    total += maxn(bank[idx+1:], n-1)
    return total


def part1(lines: list[str]) -> int:
    banks = [[int(x) for x in bank] for bank in lines]
    total = 0
    for bank in banks:
        total += maxn(bank, 2)
    return total


def part2(lines: list[str]) -> int:
    banks = [[int(x) for x in bank] for bank in lines]
    total = 0
    for bank in banks:
        total += maxn(bank, 12)
    return total


def main():
    with open("input.txt") as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
        print("Part 1:", part1(lines))
        print("Part 2:", part2(lines))


if __name__ == '__main__':
    main()
