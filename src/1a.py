import util



with open(util.get_input_path(1), "r") as f:
    inp = [int(s.strip()) for s in f.readlines()]

s = set()

for i in inp:
    s.update({2020 - i})

for j in inp:
    if j in s:
        print((2020-j) * j)
        break
