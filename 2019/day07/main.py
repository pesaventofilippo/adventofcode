from intcode import IntcodeCPU
from itertools import permutations


def part1(lines: list[str]) -> int:
    max_output = 0
    for phases in permutations([0, 1, 2, 3, 4]):
        prev_output = 0
        for phase in phases:
            cpu = IntcodeCPU.from_line(lines[0])
            cpu.add_inputs(phase, prev_output)
            prev_output = cpu.execute()[0]
        max_output = max(max_output, prev_output)
    return max_output


def part2(lines: list[str]) -> int:
    max_output = 0
    for phases in permutations([5, 6, 7, 8, 9]):
        prev_output = 0
        cpus = [IntcodeCPU.from_line(lines[0], [phases[i]]) for i in range(5)]

        while not cpus[-1].halted:
            for cpu in cpus:
                cpu.add_inputs(prev_output)
                res = cpu.execute_step()
                if res is not None:
                    prev_output = res
        max_output = max(max_output, prev_output)
    return max_output


def main():
    with open("input.txt") as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
        print("Part 1:", part1(lines))
        print("Part 2:", part2(lines))


if __name__ == '__main__':
    main()
