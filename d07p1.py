import lib
import d07
order = "23456789TJQKA"
hands = []
for s in lib.block("input/07.txt"):
    cards, bid = s.split()
    r0, r1, r2, r3, r4 = [order.find(card) for card in cards]
    hands.append((d07.htype(cards), r0, r1, r2, r3, r4, cards, int(bid)))
hands.sort()
print("ans", sum((i + 1) * hand[7] for i, hand in enumerate(hands)))
