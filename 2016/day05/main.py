from hashlib import md5


def part1(lines: list[str]) -> str:
    door_id = lines[0]
    password = ""
    i = 0
    for _ in range(8):
        while True:
            hash = md5(f"{door_id}{i}".encode()).hexdigest()
            i += 1
            if hash.startswith("00000"):
                password += hash[5]
                break
    return password


def part2(lines: list[str]) -> str:
    door_id = lines[0]
    password = ['_'] * 8
    found = set()
    i = 0
    for _ in range(8):
        while True:
            hash = md5(f"{door_id}{i}".encode()).hexdigest()
            i += 1
            if hash.startswith("00000"):
                if hash[5].isdigit() and (pos := int(hash[5])) < 8 and pos not in found:
                    password[pos] = hash[6]
                    found.add(pos)
                    break
    return ''.join(password)


def main():
    with open("input.txt") as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
        print("Part 1:", part1(lines))
        print("Part 2:", part2(lines))


if __name__ == '__main__':
    main()
