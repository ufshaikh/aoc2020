import re
import util

import functools as func
import typing as t

container_rgx = re.compile(r".+(?= bags contain)")
bags_rgx = re.compile(r" bags?\.?")
skip_span_len = len(" bags contain ")
contained_rgx = re.compile(r"(\d+ )((?:\w+ )+)bags?")


def parse_rule(rule: str) -> None:
    container_m = container_rgx.match(rule)
    assert container_m is not None
    container = container_m.group()
    e_idx = container_m.end()
    if rule.find("no other bags", e_idx) != -1:
        rules[container] = None
        return None
    contained = [(tup[1].strip(), int(tup[0])) for tup in
                 contained_rgx.findall(rule, e_idx)]
    rules[container] = contained


@func.cache
def bag_holds(holder):
    if rules[holder] is None:
        return 0
    return (sum([b[1] * bag_holds(b[0]) for b in rules[holder]])
            + sum([b[1] for b in rules[holder]]))


rules: t.Dict[str, t.Optional[t.List[t.Tuple[str, int]]]] = {}

with open(util.get_input_path(7), "r") as f:
    for line in f.readlines():
        parse_rule(line.strip())
    print(bag_holds("shiny gold"))
