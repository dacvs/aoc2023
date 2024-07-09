import lib
import d06
block = lib.block("input/06.txt")
ts = block[0].split()[1:]
ds = block[1].split()[1:]
t = int(''.join(ts))
d = int(''.join(ds))
print("ans", d06.num_ways(t, d))
