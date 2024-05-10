def hash(w):
    h = 0
    for c in w:
        h = ((h + ord(c)) * 17) % 256
    return h
