def fuel_from_mass(mass: int) -> int:
    return mass // 3 - 2


def fuel_rec(mass: int) -> int:
    fuel = fuel_from_mass(mass)
    if fuel <= 0:
        return 0
    return fuel + fuel_rec(fuel)


def part1(lines: list[str]) -> int:
    return sum(fuel_from_mass(int(l)) for l in lines)


def part2(lines: list[str]) -> int:
    return sum(fuel_rec(int(l)) for l in lines)


def main():
    with open("input.txt") as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
        print("Part 1:", part1(lines))
        print("Part 2:", part2(lines))


if __name__ == '__main__':
    main()
