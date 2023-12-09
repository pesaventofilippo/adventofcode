from itertools import combinations_with_replacement
hands: list[str] = []
bets: dict[str, int] = {}
cards = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
jokers = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2']


def rank(hand: str) -> int:
    if hand.count('J') > 3:
        return 7
    elif hand.count('J') > 0:
        nojokers = hand.replace('J', '')
        maxrank = 1
        for perm in combinations_with_replacement(jokers, hand.count('J')):
            newhand = nojokers + ''.join(perm)
            maxrank = max(maxrank, rank(newhand))
        return maxrank

    else:
        if any(hand.count(c) == 5 for c in cards):
            return 7 # Five of a kind
        if any(hand.count(c) == 4 for c in cards):
            return 6 # Four of a kind
        if any(hand.count(c) == 3 for c in cards) and any(hand.count(c) == 2 for c in cards):
            return 5 # Full house
        if any(hand.count(c) == 3 for c in cards):
            return 4 # Three of a kind
        if sum(hand.count(c) == 2 for c in cards) == 2:
            return 3 # Two pair
        if any(hand.count(c) == 2 for c in cards):
            return 2 # One pair
        return 1 # High card


def highest(first_hand: str, second_hand: str) -> str:
    r1 = rank(first_hand)
    r2 = rank(second_hand)
    if r1 > r2:
        return first_hand
    if r2 > r1:
        return second_hand

    for c1, c2 in zip(first_hand, second_hand):
        if c1 != c2:
            return first_hand if cards.index(c1) < cards.index(c2) else second_hand


with open("input.txt") as f:
    lines = [l.strip() for l in f.readlines()]
    for line in lines:
        hand, bet = line.split()
        hands.append(hand)
        bets[hand] = int(bet)


for i in range(len(hands)-1):
    for j in range(i+1, len(hands)):
        if highest(hands[i], hands[j]) == hands[i]:
            hands[i], hands[j] = hands[j], hands[i]


total = 0
for i in range(len(hands)):
    total += bets[hands[i]] * (i+1)
print(total)
