def htype(cards):
    count = {card: 0 for card in cards}
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
