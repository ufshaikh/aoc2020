import util


fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}


def is_valid_p(p):
    es = {e[0]: e[1] for e in map(lambda x: x.split(":"), p.split())}
    seen_es = set(es.keys())
    return len(fields - seen_es) == 0


with open(util.get_input_path(4), "r") as f:
    ps = f.read().split("\n\n")
    print(sum(map(is_valid_p, ps)))
