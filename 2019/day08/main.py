def part1(lines: list[str]) -> int:
    DIM = 25*6
    pixels = list(map(int, lines[0]))
    layers = [pixels[i:i+DIM] for i in range(0, len(pixels), DIM)]
    min_zeros = min(layers, key=lambda l: l.count(0))
    return min_zeros.count(1) * min_zeros.count(2)


def part2(lines: list[str]) -> int:
    DIM = 25 * 6
    pixels = list(map(int, lines[0]))
    layers = [pixels[i:i + DIM] for i in range(0, len(pixels), DIM)]

    final_image = []
    for i in range(DIM):
        for layer in layers:
            if layer[i] != 2:
                final_image.append(layer[i])
                break

    for i in range(0, DIM, 25):
        for j in range(25):
            print(" #" if final_image[i+j] else "  ", end="")
        print()


def main():
    with open("input.txt") as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
        print("Part 1:", part1(lines))
        print("Part 2:", part2(lines))


if __name__ == '__main__':
    main()
