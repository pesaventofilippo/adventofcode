def part1(lines: list[str]) -> int:
    TURN = 0 #player
    hp = 50
    mana = 500
    spells = {
        'Magic Missile': {'cost': 53, 'damage': 4, 'heal': 0, 'effect': None},
        'Drain': {'cost': 73, 'damage': 2, 'heal': 2, 'effect': None},
        'Shield': {'cost': 113, 'damage': 0, 'heal': 0, 'effect': {'duration': 6, 'armor': 7}},
        'Poison': {'cost': 173, 'damage': 0, 'heal': 0, 'effect': {'duration': 6, 'damage_per_turn': 3}},
        'Recharge': {'cost': 229, 'damage': 0, 'heal': 0, 'effect': {'duration': 5, 'mana_per_turn': 101}},
    }

    boss_hp = int(lines[0].split(": ")[1])
    boss_damage = int(lines[1].split(": ")[1])


def part2(lines: list[str]) -> int:
    pass


def main():
    with open("input.txt") as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
        print("Part 1:", part1(lines))
        print("Part 2:", part2(lines))


if __name__ == '__main__':
    main()
