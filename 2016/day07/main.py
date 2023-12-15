import re

def is_abba(string: str) -> bool:
    for i in range(len(string)-3):
        inner = string[i:i+4]
        if (inner[0] == inner[3]) and (inner[1] == inner[2]) and (inner[0] != inner[1]):
            return True
    return False

def pick_aba(string: str) -> list[str]:
    res = []
    for i in range(len(string)-2):
        aba = string[i:i+3]
        if (aba[0] == aba[2]) and (aba[0] != aba[1]):
            res.append(aba)
    return res

def is_pair(aba: str, bab: str) -> bool:
    return f"{aba[1]}{aba[0]}{aba[1]}" == bab

def supports_ssl(ip: str) -> bool:
    hypers = re.findall("\[(.*?)\]", ip)
    for hyp in hypers:
        ip = ip.replace(hyp, "")
    rest = ip.split("[]")

    aba = []
    bab = []
    for x in rest:
        aba.extend(pick_aba(x))
    for x in hypers:
        bab.extend(pick_aba(x))

    for a in aba:
        for b in bab:
            if is_pair(a, b):
                return True
    return False


def part1(lines: list[str]) -> int:
    total = 0
    for ip in lines:
        hypers = re.findall("\[(.*?)\]", ip)
        for hyp in hypers:
            ip = ip.replace(hyp, "")
        rest = ip.split("[]")

        if any(is_abba(x) for x in rest) and not any(is_abba(x) for x in hypers):
            total += 1
    return total


def part2(lines: list[str]) -> int:
    return sum(supports_ssl(ip) for ip in lines)


def main():
    with open("input.txt") as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
        print("Part 1:", part1(lines))
        print("Part 2:", part2(lines))


if __name__ == '__main__':
    main()
