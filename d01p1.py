def value(s):
    d = [c for c in s if c in "0123456789"]
    return int(d[0] + d[-1])
    
import lib
print("ans", sum(value(s) for s in lib.block("input/01.txt")))
