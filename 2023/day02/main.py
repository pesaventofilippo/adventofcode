games = {}


def is_valid(game: list[dict[str, int]]) -> bool:
    for extraction in game:
        if extraction.get("red", 0) > 12:
            return False
        if extraction.get("green", 0) > 13:
            return False
        if extraction.get("blue", 0) > 14:
            return False
    return True


def game_power(game: list[dict[str, int]]) -> bool:
    maxs = {}
    for extraction in game:
        for color, amount in extraction.items():
            maxs[color] = max(maxs.get(color, 0), amount)
    return maxs["red"] * maxs["green"] * maxs["blue"]


with open("input.txt") as f:
    total = 0
    for line in f.readlines():
        line = line.strip()

        game, data = line.split(": ")
        gamenum = int(game.split(" ")[1])
        games[gamenum] = []

        for ext in data.split("; "):
            balls = ext.split(", ")
            games[gamenum].append({
                b.split()[1]: int(b.split()[0]) for b in balls
            })

        total += game_power(games[gamenum])

    print(total)
