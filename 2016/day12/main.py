def part1(lines: list[str]) -> int:
    registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
    pc = 0
    while pc < len(lines):
        istr = lines[pc].split()
        if istr[0] == 'cpy':
            registers[istr[2]] = registers[istr[1]] if istr[1] in registers else int(istr[1])
        elif istr[0] == 'inc':
            registers[istr[1]] += 1
        elif istr[0] == 'dec':
            registers[istr[1]] -= 1
        elif istr[0] == 'jnz':
            x = registers[istr[1]] if istr[1] in registers else int(istr[1])
            if x != 0:
                pc += (int(istr[2]) - 1)
        pc += 1
    return registers['a']


def part2(lines: list[str]) -> int:
    registers = {'a': 0, 'b': 0, 'c': 1, 'd': 0}
    pc = 0
    while pc < len(lines):
        istr = lines[pc].split()
        if istr[0] == 'cpy':
            registers[istr[2]] = registers[istr[1]] if istr[1] in registers else int(istr[1])
        elif istr[0] == 'inc':
            registers[istr[1]] += 1
        elif istr[0] == 'dec':
            registers[istr[1]] -= 1
        elif istr[0] == 'jnz':
            x = registers[istr[1]] if istr[1] in registers else int(istr[1])
            if x != 0:
                pc += (int(istr[2]) - 1)
        pc += 1
    return registers['a']


def main():
    with open("input.txt") as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
        print("Part 1:", part1(lines))
        print("Part 2:", part2(lines))


if __name__ == '__main__':
    main()
