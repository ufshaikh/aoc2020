import re
import util


pw_re = re.compile(r"(?<=: )\w+$")
num_re = re.compile(r"\d+")
let_re = re.compile(r"\w+(?=:)")


def is_valid(s):
    pos1_m = num_re.search(s)
    pos1 = int(pos1_m.group())
    pos2_m = num_re.search(s, pos1_m.end())
    pos2 = int(pos2_m.group())
    let_m = let_re.search(s, pos2_m.end())
    let = let_m.group()
    pw = pw_re.search(s, let_m.end()).group()
    return (pw[pos1-1] == let) ^ (pw[pos2-1] == let)


with open(util.get_input_path(2), "r") as f:
    inp = [s.strip() for s in f.readlines()]
    print(sum(map(is_valid, inp)))
