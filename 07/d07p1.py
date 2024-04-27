import d07
with open("input.txt") as f:
    order = "23456789TJQKA"
    hands = []
    for s in f:
        cards, bid = s.split()
        bid = int(bid)
        r0, r1, r2, r3, r4 = [order.find(card) for card in cards]
        hands.append((d07.htype(cards), r0, r1, r2, r3, r4, cards, bid))
    hands.sort()
    ans = sum((i + 1) * hand[7] for i, hand in enumerate(hands))
    print("ans", ans)
