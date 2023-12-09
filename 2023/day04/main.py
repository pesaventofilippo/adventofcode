WON_CARDS: dict[int, int] = {}


with open("input.txt") as f:
    total = 0
    for line in f.readlines():
        line = line.strip()

        card, data = line.split(": ")
        cardnum = int(card.split(" ")[-1])
        card_multiplier = WON_CARDS.get(cardnum, 0) + 1

        wnum, cnum = data.split(" | ")
        winning_nums = [int(x) for x in wnum.split(" ") if x]
        card_nums = [int(x) for x in cnum.split(" ") if x]

        count = 0
        for num in winning_nums:
            if num in card_nums:
                count += 1

        if count > 0:
            for c in range(cardnum+1, cardnum+1+count):
                WON_CARDS[c] = WON_CARDS.get(c, 0) + card_multiplier

        total += card_multiplier

    print(total)
