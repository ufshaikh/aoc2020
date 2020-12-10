import util
import functools as func


with open(util.get_input_path(10), "r") as f:
    inp = [int(s) for s in f.readlines()]

inp = sorted(inp)
inp.append(inp[-1]+3)
inp.reverse()
inp.append(0)


length = len(inp)
@func.cache
def ways(i):
    if i == length - 1:
        return 1
    w = 0
    for s in range(1,4):
        if (i + s) < length and inp[i] - inp[i + s] <= 3:
            w += ways(i + s)
    return w

print(ways(0))
