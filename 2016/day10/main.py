def part1(lines: list[str]) -> int:
    bots = {}
    moves = {}
    for instruction in lines:
        isplit = instruction.split()
        if instruction.startswith("value "):
            value = int(isplit[1])
            bot = int(isplit[5])
            if bot in bots:
                bots[bot].append(value)
            else:
                bots[bot] = [value]
        elif instruction.startswith("bot "):
            bot = int(isplit[1])
            is_bot_1 = isplit[5] == "bot"
            bot_1 = int(isplit[6])
            is_bot_2 = isplit[10] == "bot"
            bot_2 = int(isplit[11])
            moves[bot] = (bot_1 if is_bot_1 else None, bot_2 if is_bot_2 else None)
    while full_bots := [b for b in bots if len(bots[b]) == 2]:
        for bot in full_bots:
            chips = bots[bot]
            if 61 in chips and 17 in chips:
                return bot
            del bots[bot]
            move = moves[bot]
            if move[0] is not None:
                if move[0] in bots:
                    bots[move[0]].append(min(chips))
                else:
                    bots[move[0]] = [min(chips)]
            if move[1] is not None:
                if move[1] in bots:
                    bots[move[1]].append(max(chips))
                else:
                    bots[move[1]] = [max(chips)]
    return None


def part2(lines: list[str]) -> int:
    bots = {}
    moves = {}
    outputs = {}
    for instruction in lines:
        isplit = instruction.split()
        if instruction.startswith("value "):
            value = int(isplit[1])
            bot = int(isplit[5])
            if bot in bots:
                bots[bot].append(value)
            else:
                bots[bot] = [value]
        elif instruction.startswith("bot "):
            bot = int(isplit[1])
            is_bot_1 = isplit[5] == "bot"
            bot_1 = int(isplit[6])
            is_bot_2 = isplit[10] == "bot"
            bot_2 = int(isplit[11])
            moves[bot] = (bot_1 if is_bot_1 else -bot_1-1, bot_2 if is_bot_2 else -bot_2-1)

    while full_bots := [b for b in bots if len(bots[b]) == 2]:
        for bot in full_bots:
            chips = bots[bot]
            move = moves[bot]
            del bots[bot]

            if (m := move[0]) >= 0:
                if m in bots:
                    bots[m].append(min(chips))
                else:
                    bots[m] = [min(chips)]
            else:
                outputs[-m-1] = min(chips)

            if (m := move[1]) >= 0:
                if m in bots:
                    bots[m].append(max(chips))
                else:
                    bots[m] = [max(chips)]
            else:
                outputs[-m-1] = max(chips)

    return outputs[0] * outputs[1] * outputs[2]


def main():
    with open("input.txt") as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
        print("Part 1:", part1(lines))
        print("Part 2:", part2(lines))


if __name__ == '__main__':
    main()
