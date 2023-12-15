def part1(lines: list[str]) -> int:
    floors: list[list[tuple[str, str]]] = {
        0: [("promethium", "G"), ("promethium", "M")],
        1: [("cobalt", "G"), ("curium", "G"), ("ruthenium", "G"), ("plutonium", "G")],
        2: [("cobalt", "M"), ("curium", "M"), ("ruthenium", "M"), ("plutonium", "M")],
        3: []
    }



def part2(lines: list[str]) -> int:
    pass


def main():
    with open("input.txt") as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
        print("Part 1:", part1(lines))
        print("Part 2:", part2(lines))


if __name__ == '__main__':
    main()
