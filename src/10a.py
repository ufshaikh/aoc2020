import util
with open(util.get_input_path(10), "r") as f:
    inp = [int(s) for s in f.readlines()]

inp = sorted(inp)

one = 0
three = 0
prev = 0

for i in inp:
    diff = i - prev
    if diff == 1:
        one += 1
    if diff == 3:
        three += 1
    prev = i

three += 1  # for the device
print(one * three)
