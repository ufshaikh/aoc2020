from collections import Counter

import util


with open(util.get_input_path(9), "r") as f:
    inp = [int(s) for s in f.readlines()]

l = len(inp)
c = Counter(inp[:25])

for i in range(25, l):
    elem = inp[i]
    if not any([((elem-elem_) in c) for elem_ in inp[i-25:i]]):
        target = elem
        break
    to_remove = inp[i-25]
    c[to_remove] -= 1
    if c[to_remove] < 1:
        del c[to_remove]
    c[elem] += 1

# part 2; needs target from part 1

i = 0
j = 1
sum_so_far = inp[0] + inp[1]

while sum_so_far != target:
    if sum_so_far > target and i + 1 < j:
        sum_so_far -= inp[i]
        i += 1
    else:
        j += 1
        sum_so_far += inp[j]

print(max(inp[i:j+1]) + min(inp[i:j+1]))
