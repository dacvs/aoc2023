import d20
flip, conj, outs, mem = d20.flip_conj_outs_mem()
i = 0
Q = []  # Q: queue of pulses; Q[i] is next pulse to process, if i < len(Q)
for presses in range(1000):
    Q.append(("button", 0, "broadcaster"))
    while i < len(Q):
        # pulse is triple (s, k, t); s=source; k=kind(lo=0, hi=1); t=target
        s, k, t = Q[i]
        d20.process_pulse(flip, conj, outs, mem, Q, s, k, t)
        i += 1
lo = sum(1 for q in Q if q[1] == 0)
hi = sum(1 for q in Q if q[1] == 1)
print("ans", lo * hi)
