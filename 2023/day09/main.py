def extrapolate(history: list[int]) -> list[int]:
    return [history[i+1]-history[i] for i in range(len(history)-1)]

def last_elem(history: list[int]) -> int:
    if all(x == 0 for x in history):
        return 0
    return history[-1] + last_elem(extrapolate(history))

def prev_elem(history: list[int]) -> int:
    if all(x == 0 for x in history):
        return 0
    return history[0] - prev_elem(extrapolate(history))


def part1(lines: list[str]) -> int:
    histories: list[list[int]] = [[int(x) for x in line.split()] for line in lines]
    return sum(last_elem(h) for h in histories)


def part2(lines: list[str]) -> int:
    histories: list[list[int]] = [[int(x) for x in line.split()] for line in lines]
    return sum(prev_elem(h) for h in histories)


def main():
    with open("input.txt") as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
        print("Part 1:", part1(lines))
        print("Part 2:", part2(lines))


if __name__ == '__main__':
    main()
