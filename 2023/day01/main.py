maps = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}


def extract_digits(line: str) -> list[int]:
    while any(k in line for k in maps.keys()):
        appear_indexes = {
            k: line.find(k) for k in maps.keys() if line.find(k) > -1
        }
        idx = min(appear_indexes, key=appear_indexes.get)
        line = line.replace(idx, maps[idx], 1)

    return [int(x) for x in line if x.isdigit()]


def extract_digits_reversed(line: str) -> list[int]:
    while any(k in line for k in maps.keys()):
        appear_indexes = {
            k: line.rfind(k) for k in maps.keys() if line.rfind(k) > -1
        }
        idx = max(appear_indexes, key=appear_indexes.get)
        line = line[:appear_indexes[idx]] + line[appear_indexes[idx]:].replace(idx, maps[idx], 1)

    return [int(x) for x in line if x.isdigit()]


with open("input.txt") as f:
    total = 0
    for line in f.readlines():
        line = line.strip()
        digits = extract_digits(line)
        rev_digits = extract_digits_reversed(line)
        total += digits[0]*10 + rev_digits[-1]

    print(total)
