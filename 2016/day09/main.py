import re

def part1(lines: list[str]) -> int:
    text = lines[0].replace(" ", "")
    while markers := re.findall("\((.*?)\)", text):
        mk = markers[0]
        mk_start = text.find(f"({mk})")
        rep_start = mk_start + len(mk) + 2
        mk_len, mk_rep = map(int, mk.split('x'))

        text_to_repeat = (text[rep_start:rep_start+mk_len]).replace("(", "<").replace(")", ">")
        text = text[:mk_start] + text_to_repeat * mk_rep + text[rep_start+len(text_to_repeat):]
    return len(text)


def part2(lines: list[str]) -> int:
    text = lines[0].replace(" ", "")
    while markers := re.findall("\((.*?)\)", text):
        mk = markers[0]
        mk_start = text.find(f"({mk})")
        rep_start = mk_start + len(mk) + 2
        mk_len, mk_rep = map(int, mk.split('x'))

        text_to_repeat = (text[rep_start:rep_start + mk_len])
        text = text[:mk_start] + text_to_repeat * (mk_rep-1) + text[rep_start:]
    return len(text)


def main():
    with open("input.txt") as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
        print("Part 1:", part1(lines))
        print("Part 2:", part2(lines))


if __name__ == '__main__':
    main()
