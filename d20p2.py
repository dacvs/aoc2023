import d20
import numpy as np
flip, conj, outs, mem = d20.flip_conj_outs_mem()

# NOTE: rx is the final module
# According to the problem statement, the final machine activates when rx receives Lo.

ans = +np.inf
for rxp in outs:
    if "rx" in outs[rxp]:   # so that rxp is a pred of rx
        assert rxp in conj  # our particular input has only conj before rx

        # We want to know when rx receives Lo.
        # This occurs when the first predecessor of rx sends Lo.
        # Each predecessor rxp of rx is of type conj.
        # We expect the value (Lo or Hi) at each module to be periodic.
        # As rxp is conj, we want to know when each predecessor rxpp of rxp is Hi.

        fmpp = set(s for s in outs if rxp in outs[s])   # final module pred preds
        i = 0
        Q = []  # Q: queue of pulses; Q[i] is the next pulse to process, if i < len(Q)
        period = {}
        p = 0   # number of button presses
        while period.keys() != fmpp:
            p += 1
            Q.append(("button", 0, "broadcaster"))
            while i < len(Q):
                # pulse is triple (s, k, t); s=source; k=kind(lo=0, hi=1); t=target
                s, k, t = Q[i]
                d20.process_pulse(flip, conj, outs, mem, Q, s, k, t)
                if t == rxp and k == 1:
                    if not s in period:
                        period[s] = p
                i += 1
        a = np.lcm.reduce(list(period.values()))
        if ans > a:
            ans = a
print(f"ans", ans)
