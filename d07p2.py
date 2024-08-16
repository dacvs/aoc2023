import lib
import d07

def mhtype(M, order, cards):  # memoized
    j = cards.find('J')
    if j < 0:
        return d07.htype(cards)
    if not cards in M:
        M[cards] = max(
            mhtype(M, order, cards[:j] + card + cards[j+1:])
            for card in order[1:]
        )
    return M[cards]

order = "J23456789TQKA"
M = {}  # Key is hand, like "32TJK". Val is highest value achieved by resolving wildcards.
hands = []
for s in lib.block("input/07.txt"):
    cards, bid = s.split()
    r0, r1, r2, r3, r4 = [order.find(card) for card in cards]
    hands.append((mhtype(M, order, cards), r0, r1, r2, r3, r4, cards, int(bid)))
hands.sort()
print("ans", sum((i + 1) * hand[7] for i, hand in enumerate(hands)))
