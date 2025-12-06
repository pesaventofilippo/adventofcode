def part1(lines: list[str]) -> int:
    fresh_ranges = []
    ingredients = []
    for line in lines:
        if "-" in line:
            fresh_ranges.append((int(line.split("-")[0]), int(line.split("-")[1])))
        else:
            ingredients.append(int(line))

    def is_fresh(ingredient: int) -> bool:
        for (start, end) in fresh_ranges:
            if start <= ingredient <= end:
                return True
        return False

    return sum(1 for i in ingredients if is_fresh(i))


def part2(lines: list[str]) -> int:
    ranges = []
    for line in lines:
        if "-" in line:
            ranges.append((int(line.split("-")[0]), int(line.split("-")[1])))

    ranges.sort()
    discreet = set()
    curr_start, curr_end = ranges[0]
    for (start, end) in ranges[1:]:
        if start <= curr_end+1:
            curr_end = max(curr_end, end)
        else:
            discreet.add((curr_start, curr_end))
            curr_start, curr_end = start, end
    discreet.add((curr_start, curr_end))

    total = 0
    for (start, end) in discreet:
        total += end - start + 1
    return total


def main():
    with open("input.txt") as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
        print("Part 1:", part1(lines))
        print("Part 2:", part2(lines))


if __name__ == '__main__':
    main()
