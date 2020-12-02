import sys
import util


with open(util.get_input_path(1), "r") as f:
    inp = [int(s.strip()) for s in f.readlines()]


for i in inp:
    target = 2020 - i
    s = set()

    for j in inp:
        s.update({target - j})

    for k in inp:
        if k in s:
            print((target - k) * k * i)
            sys.exit(0)
