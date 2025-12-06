from intcode import execute


def part1(lines: list[str]) -> int:
    mem = list(map(int, lines[0].split(",")))
    mem[1] = 12
    mem[2] = 2
    res = execute(mem)
    return res[0]


def part2(lines: list[str]) -> int:
    mem = list(map(int, lines[0].split(",")))
    for i in range(100):
        for j in range(100):
            mem[1] = i
            mem[2] = j
            res = execute(mem)
            if res[0] == 19690720:
                return 100 * i + j


def main():
    with open("input.txt") as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
        print("Part 1:", part1(lines))
        print("Part 2:", part2(lines))


if __name__ == '__main__':
    main()
