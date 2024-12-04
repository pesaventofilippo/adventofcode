def part1(lines: list[str]) -> int:
    def find_xmas(x: int, y: int, dir: str, step: int=0) -> bool:
        if y < 0 or y >= len(lines) or x < 0 or x >= len(lines[y]):
            return False

        letter = "XMAS"[step]
        if lines[y][x] != letter:
            return False
        if step == 3:
            return True

        if "N" in dir:
            y -= 1
        if "E" in dir:
            x += 1
        if "S" in dir:
            y += 1
        if "W" in dir:
            x -= 1

        return find_xmas(x, y, dir, step+1)

    total = 0
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            for dir in ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]:
                total += find_xmas(x, y, dir)
    return total


def part2(lines: list[str]) -> int:
    centers: list[tuple[int, int]] = []

    def find_xmas(x: int, y: int, dir: str, step: int = 0, center: tuple[int, int] = None) -> bool:
        if y < 0 or y >= len(lines) or x < 0 or x >= len(lines[y]):
            return False

        letter = "MAS"[step]
        if lines[y][x] != letter:
            return False
        if step == 1:
            center = (x, y)
        if step == 2:
            if center in centers:
                return True
            else:
                centers.append(center)
                return False

        if "N" in dir:
            y -= 1
        if "E" in dir:
            x += 1
        if "S" in dir:
            y += 1
        if "W" in dir:
            x -= 1

        return find_xmas(x, y, dir, step+1, center)

    total = 0
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            for dir in ["NE", "SE", "SW", "NW"]:
                total += find_xmas(x, y, dir)
    return total


def main():
    with open("input.txt") as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
        print("Part 1:", part1(lines))
        print("Part 2:", part2(lines))


if __name__ == '__main__':
    main()
