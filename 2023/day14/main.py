from functools import cache

@cache
def transpose(lines: tuple[str], reverse: bool=False) -> tuple[str]:
    _range = range(len(lines[0])-1, -1, -1) if reverse else range(len(lines[0]))
    return tuple(''.join(row[j] for row in lines) for j in _range)

@cache
def roll_line(line: str) -> str:
    return "#".join(''.join(sorted(b, reverse=True)) for b in line.split("#"))

@cache
def roll_all(lines: tuple[str]) -> tuple[str]:
    return transpose(tuple(roll_line(row) for row in transpose(lines)))


def part1(lines: list[str]) -> int:
    lines = roll_all(tuple(lines))
    return sum((len(lines)-i)*lines[i].count("O") for i in range(len(lines)))


def part2(lines: list[str]) -> int:
    lines = tuple(lines)
    for _ in range(1000000000*4):
        lines = roll_all(lines)
        lines = transpose(lines, reverse=True)
    return sum((len(lines)-i)*lines[i].count("O") for i in range(len(lines)))


def main():
    with open("input.txt") as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
        print("Part 1:", part1(lines))
        print("Part 2:", part2(lines))


if __name__ == '__main__':
    main()
