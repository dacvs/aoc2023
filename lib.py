def blocks(filename):
    with open(filename) as f:
        for block in f.read().split("\n\n"):
            yield [line for line in block.split("\n") if line]

def block(filename):  # when only 1 block is expected
    return next(blocks(filename))

def split(line, seps):
    out = []
    for sep in seps:
        pre, line = line.split(sep, maxsplit=1)
        out.append(pre)
    return out + [line]
