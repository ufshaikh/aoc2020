import util


with open(util.get_input_path(3), "r") as f:
    inp = [s.strip() for s in f.readlines()]


def f(v_y, v_x):
    y = 0
    x = 0
    count = 0
    h = 323  # height of input
    w = len(inp[0])  # width of input
    while y < h:
        # I don't think 0,0 counts, but there's no tree there anyway
        if inp[y][x] == "#":
            count += 1
        x += v_x
        x %= w
        y += v_y
    return count


print(f(1, 3))
