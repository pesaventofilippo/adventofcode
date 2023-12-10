def is_real(room: str, checksum: str) -> bool:
    real_csum = ""
    counts = {c: room.count(c) for c in room}
    top_5 = sorted(counts.values(), reverse=True)[:5]

    for count in top_5:
        best_so_far = "z"
        for c in [c for c in room if counts.get(c, -1) == count]:
            best_so_far = min(best_so_far, c)
        real_csum += best_so_far
        del counts[best_so_far]

    return checksum == real_csum


def part1(lines: list[str]) -> int:
    total = 0
    for room in lines:
        raw = room.split('-')
        name = "".join(raw[:-1])
        sid, csum = raw[-1].split('[')
        sid = int(sid)
        csum = csum.replace("]", "")

        if is_real(name, csum):
            total += sid

    return total


def part2(lines: list[str]) -> int:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for room in lines:
        raw = room.split('-')
        name = " ".join(raw[:-1])
        sid, _ = raw[-1].split('[')
        sid = int(sid)

        name = [alphabet[(alphabet.index(c)+sid)%26] if c != " " else " " for c in name]
        if "".join(name) == "northpole object storage":
            return sid


def main():
    with open("input.txt") as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
        print("Part 1:", part1(lines))
        print("Part 2:", part2(lines))


if __name__ == '__main__':
    main()
