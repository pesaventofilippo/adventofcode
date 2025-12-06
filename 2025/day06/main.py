def part1(lines: list[str]) -> int:
    inputs = [[x for x in line.split()] for line in lines]
    data = [[inp[i] for inp in inputs] for i in range(len(inputs[0]))]

    total = 0
    for *nums, op in data:
        if op == '+':
            result = 0
            for n in nums:
                result += int(n)
        elif op == '*':
            result = 1
            for n in nums:
                result *= int(n)
        total += result
    return total


def part2(lines: list[str]) -> int:
    maxl = max([len(x) for x in lines])
    for i in range(len(lines)):
        if len(lines[i]) != maxl:
            lines[i] += ' ' * (maxl - len(lines[i]))

    total = 0
    lines = [line[::-1] for line in lines]
    nums = []
    for pointer in range(maxl):
        if all(lines[i][pointer] == ' ' for i in range(len(lines))):
            nums = []
            continue

        num = ""
        for i in range(len(lines)-1):
            num += lines[i][pointer].replace(" ", "")
        nums.append(int(num))

        if lines[-1][pointer] != ' ':
            op = lines[-1][pointer]
            if op == '+':
                result = 0
                for n in nums:
                    result += n
            elif op == '*':
                result = 1
                for n in nums:
                    result *= n
            nums = []
            total += result

    return total


def main():
    with open("input.txt") as f:
        lines = [l.strip("\n") for l in f.readlines() if l.strip("\n")]
        print("Part 1:", part1(lines))
        print("Part 2:", part2(lines))


if __name__ == '__main__':
    main()
