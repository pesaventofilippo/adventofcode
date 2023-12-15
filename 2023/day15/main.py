def HASH(string: str) -> int:
    n = 0
    for c in string:
        n += ord(c)
        n *= 17
        n %= 256
    return n


def part1(lines: list[str]) -> int:
    steps = lines[0].split(",")
    return sum(HASH(s) for s in steps)


def part2(lines: list[str]) -> int:
    boxes: dict[int, list[tuple[str, int]]] = {}
    steps = lines[0].split(",")
    for step in steps:
        if "-" in step:
            label = step.split("-")[0]
            box = HASH(label)
            if box in boxes:
                lenses = [i for (i, x) in enumerate(boxes[box]) if x[0] == label]
                if lenses:
                    boxes[box].pop(lenses[0])
        elif "=" in step:
            label = step.split("=")[0]
            length = int(step.split("=")[1])
            box = HASH(label)
            if box in boxes:
                lenses = [i for (i, x) in enumerate(boxes[box]) if x[0] == label]
                if lenses:
                    boxes[box][lenses[0]] = (label, length)
                else:
                    boxes[box].append((label, length))
            else:
                boxes[box] = [(label, length)]

    total = 0
    for box in boxes:
        for i, (_, lens) in enumerate(boxes[box]):
            total += (1+box) * (1+i) * lens
    return total

def main():
    with open("input.txt") as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
        print("Part 1:", part1(lines))
        print("Part 2:", part2(lines))


if __name__ == '__main__':
    main()
