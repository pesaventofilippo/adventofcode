from hashlib import md5
from functools import cache

@cache
def hash(salt: str, index: int) -> int:
    return md5(f"{salt}{index}".encode()).hexdigest()

@cache
def stretched_hash(salt: str, index: int) -> int:
    result = hash(salt, index)
    for _ in range(2016):
        result = md5(result.encode()).hexdigest()
    return result

@cache
def has_repeating(s: str, n: int) -> str:
    for i in range(len(s) - n + 1):
        if all(s[i] == s[i + j] for j in range(1, n)):
            return s[i]
    return None


def part1(lines: list[str]) -> int:
    salt = lines[0]
    valid = []
    index = -1
    while len(valid) < 64:
        index += 1
        key = hash(salt, index)
        if not (c := has_repeating(key, 3)):
            continue
        for i in range(index+1, index+1001):
            next_key = hash(salt, i)
            if has_repeating(next_key, 5) == c:
                valid.append(index)
                break
    return index


def part2(lines: list[str]) -> int:
    salt = lines[0]
    valid = []
    index = -1
    while len(valid) < 64:
        index += 1
        key = stretched_hash(salt, index)
        if not (c := has_repeating(key, 3)):
            continue
        for i in range(index + 1, index + 1001):
            next_key = stretched_hash(salt, i)
            if has_repeating(next_key, 5) == c:
                valid.append(index)
                break
    return index


def main():
    with open("input.txt") as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
        print("Part 1:", part1(lines))
        print("Part 2:", part2(lines))


if __name__ == '__main__':
    main()
