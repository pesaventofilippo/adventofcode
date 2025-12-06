from intcode import IntcodeCPU

def part1(lines: list[str]) -> int:
    cpu = IntcodeCPU.from_line(lines[0])
    cpu.add_inputs(1)
    print(cpu.execute()[0])


def part2(lines: list[str]) -> int:
    cpu = IntcodeCPU.from_line(lines[0])
    cpu.add_inputs(2)
    print(cpu.execute()[0])


def main():
    with open("input.txt") as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
        print("Part 1:", part1(lines))
        print("Part 2:", part2(lines))


if __name__ == '__main__':
    main()
