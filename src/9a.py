from collections import Counter

import util


with open(util.get_input_path(9), "r") as f:
    inp = [int(s) for s in f.readlines()]

l = len(inp)
c = Counter(inp[:25])

for i in range(25, l):
    elem = inp[i]
    if not any([elem-elem_ in c and elem_ * 2 != elem for elem_ in inp[i-25:i]]):
        print(elem)
        break
    to_remove = inp[i-25]
    c[to_remove] -= 1
    if c[to_remove] < 1:
        del c[to_remove]
    c[elem] += 1
