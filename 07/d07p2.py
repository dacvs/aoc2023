ranks = "J23456789TQKA"


def htype(cards):
    count = {card: 0 for card in ranks}
    for card in cards:
        count[card] += 1
    freq = tuple(n for n in sorted(count.values(), reverse=True) if n)
    D = {
        (5,):               6,
        (4, 1):             5,
        (3, 2):             4,
        (3, 1, 1):          3,
        (2, 2, 1):          2,
        (2, 1, 1, 1):       1,
        (1, 1, 1, 1, 1):    0}
    return D[freq]


def mhtype(M, cards):  # memoized
    j = cards.find('J')
    if j < 0:
        return htype(cards)
    if not cards in M:
        M[cards] = max(mhtype(M, cards[:j] + card + cards[j+1:]) for card in ranks[1:])
    return M[cards]


with open("input.txt") as f:
    M = {}  # key is hand, like "32TJK". val is highest value achieved by resolving wildcards
    hands = []
    for s in f:
        cards, bid = s.split()
        bid = int(bid)
        r0, r1, r2, r3, r4 = [ranks.find(card) for card in cards]
        hands.append((mhtype(M, cards), r0, r1, r2, r3, r4, cards, bid))
    hands.sort()
    ans = sum((i + 1) * hand[7] for i, hand in enumerate(hands))
    print("ans", ans)
