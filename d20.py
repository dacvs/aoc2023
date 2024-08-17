import lib

def flip_conj_outs_mem():
    flip = {}
    conj = {}
    outs = {}
    for line in lib.block("input/20.txt"):  # line is like "%cg -> mt, hb"
        s, T = lib.split(line, [" -> "])    # s: source; T: targets
        outs[s.lstrip("%&")] = T.split(", ")
        if s[0] == '%': flip[s[1:]] = 0     # 0: this flip-flop is off
        if s[0] == '&': conj[s[1:]] = []
    assert outs.keys() == set(["broadcaster"]) | flip.keys() | conj.keys()
    assert not flip.keys() & conj.keys()

    # conj[t] is the list of inputs to t (if t is a conjunction)
    for s in outs:
        for t in outs[s]:
            if t in conj:
                conj[t].append(s)

    mem = {(s, t): 0 for t in conj for s in conj[t]}
    return flip, conj, outs, mem

def process_pulse(flip, conj, outs, mem, Q, s, k, t):
    """Process pulse (s, k, t) and modify flip, mem, and Q accordingly"""
    if t == "broadcaster":
        for u in outs[t]:
            Q.append((t, k, u))
    if t in flip and k == 0:
        flip[t] = 1 - flip[t]
        for u in outs[t]:
            Q.append((t, flip[t], u))
    if t in conj:
        mem[s, t] = k
        n = 0 if all(mem[r, t] for r in conj[t]) else 1  # nand
        for u in outs[t]:
            Q.append((t, n, u))
