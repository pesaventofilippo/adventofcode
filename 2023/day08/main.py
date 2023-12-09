def part1(lines: list[str]) -> int:
    instructions: list[int] = [0 if char == 'L' else 1 for char in lines[0]]
    MAP: dict[str, tuple[str, str]] = {}
    for node in lines[1:]:
        name, dest = node.split(" = ")
        dest_left, dest_right = dest[1:-1].split(", ")
        MAP[name] = (dest_left, dest_right)

    steps = 0
    current_pos = 'AAA'
    while current_pos != 'ZZZ':
        direction = instructions[steps % len(instructions)]
        current_pos = MAP[current_pos][direction]
        steps += 1
    return steps

def part2(lines: list[str]) -> int:
    from math import lcm
    instructions: list[int] = [0 if char == 'L' else 1 for char in lines[0]]
    MAP: dict[str, tuple[str, str]] = {}
    for node in lines[1:]:
        name, dest = node.split(" = ")
        dest_left, dest_right = dest[1:-1].split(", ")
        MAP[name] = (dest_left, dest_right)

    starting_nodes = [n for n in MAP.keys() if n.endswith('A')]
    loop_lengths: list[int] = []
    for node in starting_nodes:
        current_node = node
        history = []
        steps = 0

        while True:
            ipointer = steps % len(instructions)
            next_direction = instructions[ipointer]
            next_node = MAP[current_node][next_direction]

            if (next_node, ipointer) in history:
                # We already visited next_node, and no matter the next direction, the result would be the same
                loop_start = history.index((next_node, ipointer))
                loop = history[loop_start:]

                loop_lengths.append(len(loop))
                break

            steps += 1
            current_node = next_node
            history.append((current_node, ipointer))

    # End positions solve the following formula: ((pos - loop[0]) % loop[1]) == loop[2]
    return lcm(*loop_lengths)


def main():
    with open("input.txt") as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
        print("Part 1:", part1(lines))
        print("Part 2:", part2(lines))


if __name__ == '__main__':
    main()
