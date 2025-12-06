from functools import cache

def part1(lines: list[str]) -> int:
    nodes = {}
    for line in lines:
        target, obj = line.split(")")
        nodes[obj] = target

    @cache
    def count_orbits(node):
        if node not in nodes:
            return 0
        return 1 + count_orbits(nodes[node])

    return sum(count_orbits(node) for node in nodes)


def part2(lines: list[str]) -> int:
    nodes = {}
    for line in lines:
        target, obj = line.split(")")
        nodes[obj] = target

    start = nodes["YOU"]
    end = nodes["SAN"]

    def path_to_root(node):
        path = []
        while node in nodes:
            path.append(node)
            node = nodes[node]
        return path

    path_start = path_to_root(start)
    path_end = path_to_root(end)

    common = 0
    for a, b in zip(reversed(path_start), reversed(path_end)):
        if a != b:
            break
        common += 1

    return len(path_start) + len(path_end) - 2*common


def main():
    with open("input.txt") as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
        print("Part 1:", part1(lines))
        print("Part 2:", part2(lines))


if __name__ == '__main__':
    main()
