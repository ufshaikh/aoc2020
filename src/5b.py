from collections import defaultdict
from typing import DefaultDict, Tuple
import util


def code_to_seat(c: str) -> Tuple[int, int]:
    table = c.maketrans("RLFB", "1001")
    c = c.translate(table)
    row = int(c[0:7], 2)
    col = int(c[7:], 2)
    return row, col


with open(util.get_input_path(5), "r") as f:
    inp = [s.strip() for s in f.readlines()]
    d: DefaultDict[int, DefaultDict[int, int]] = defaultdict(lambda: defaultdict(int))
    for i in inp:
        r, c = code_to_seat(i)
        d[r][c] = 1

    # print seating:
    print("1234 5678")
    print("____ ____")
    print("")
    for j in range(128):
        for k in range(8):
            if k == 4:
                print(" ", end="")
            print(d[j][k], end="")
        print("\t| ", j)
