def part1(lines: list[str]) -> int:
    manifold = [[x for x in line] for line in lines]
    splits = 0
    for i in range(1, len(manifold)):
        for j in range(len(manifold[i])):
            if manifold[i-1][j] in ['S', '|']:
                if manifold[i][j] == '^':
                    manifold[i][j-1] = manifold[i][j+1] = '|'
                    splits += 1
                else:
                    manifold[i][j] = '|'

    return splits


def part2(lines: list[str]) -> int:
    manifold = [[1 if x=='S' else 0 if x=='.' else x for x in line]
                for line in lines if not all(c in "." for c in line)]

    for i in range(1, len(manifold)):
        for j in range(len(manifold[i])):
            if manifold[i - 1][j] not in ['^', 0]:
                if manifold[i][j] == '^':
                    manifold[i][j - 1] += manifold[i - 1][j]
                    manifold[i][j + 1] += manifold[i - 1][j]
                else:
                    manifold[i][j] += manifold[i - 1][j]

    return sum(x for x in manifold[-1] if x != '^')


def main():
    with open("input.txt") as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
        print("Part 1:", part1(lines))
        print("Part 2:", part2(lines))


if __name__ == '__main__':
    main()
