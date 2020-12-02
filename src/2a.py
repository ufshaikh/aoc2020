import re
import util


pw_re = re.compile(r"(?<=: )\w+$")
num_re = re.compile(r"\d+")
let_re = re.compile(r"\w+(?=:)")


def is_valid(s):
    lo_m = num_re.search(s)
    lo = int(lo_m.group())
    hi_m = num_re.search(s, lo_m.end())
    hi = int(hi_m.group())
    let_m = let_re.search(s, hi_m.end())
    let = let_m.group()
    pw = pw_re.search(s, let_m.end()).group()
    let_count = pw.count(let)
    return lo <= let_count <= hi


with open(util.get_input_path(2), "r") as f:
    inp = [s.strip() for s in f.readlines()]
    print(sum(map(is_valid, inp)))
