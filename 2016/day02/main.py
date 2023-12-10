def part1(lines: list[str]) -> str:
    KEYPAD = [
        "123",
        "456",
        "789"
    ]

    button = (1, 1)
    code = ""
    for line in lines:
        for direction in line:
            if direction == "U":
                new_btn = (max(0, button[0]-1), button[1])
            elif direction == "D":
                new_btn = (min(2, button[0]+1), button[1])
            elif direction == "L":
                new_btn = (button[0], max(0, button[1]-1))
            elif direction == "R":
                new_btn = (button[0], min(2, button[1]+1))

            if KEYPAD[new_btn[0]][new_btn[1]] != "0":
                button = new_btn
        code += KEYPAD[button[0]][button[1]]
    return code


def part2(lines: list[str]) -> str:
    KEYPAD = [
        "00100",
        "02340",
        "56789",
        "0ABC0",
        "00D00"
    ]

    button = (1, 1)
    code = ""
    for line in lines:
        for direction in line:
            if direction == "U":
                new_btn = (max(0, button[0] - 1), button[1])
            elif direction == "D":
                new_btn = (min(4, button[0] + 1), button[1])
            elif direction == "L":
                new_btn = (button[0], max(0, button[1] - 1))
            elif direction == "R":
                new_btn = (button[0], min(4, button[1] + 1))

            if KEYPAD[new_btn[0]][new_btn[1]] != "0":
                button = new_btn
        code += KEYPAD[button[0]][button[1]]
    return code


def main():
    with open("input.txt") as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
        print("Part 1:", part1(lines))
        print("Part 2:", part2(lines))


if __name__ == '__main__':
    main()
