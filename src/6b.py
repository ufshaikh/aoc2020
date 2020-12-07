from collections import defaultdict
from typing import DefaultDict, Tuple
import util


def count(i: str) -> int:
    return len(util.big_intersection([set(p) for p in (i.split("\n"))]))


with open(util.get_input_path(6), "r") as f:
    inp = f.read().strip().split("\n\n")
    print(sum([count(i) for i in inp]))
