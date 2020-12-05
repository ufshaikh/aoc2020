import util


def code_to_id(c: str) -> int:
    table = c.maketrans("RLFB", "1001")
    c = c.translate(table)
    row = int(c[0:7], 2)
    col = int(c[7:], 2)
    return row * 8 + col


with open(util.get_input_path(5), "r") as f:
    inp = [s.strip() for s in f.readlines()]
    print(max(map(code_to_id, inp)))
