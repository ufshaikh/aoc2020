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
def is_ancestor_of(bag: str, my_bag: str) -> bool:
    if rules[bag] is None:
        return False
    t = rules[bag]  # mypy needs a temporary here
    assert t is not None
    if any(b[0] == my_bag for b in t):
        return True
    return any([is_ancestor_of(b[0], my_bag) for b in t])


def how_many_ancestors(my_bag: str) -> int:
    return sum([is_ancestor_of(r, my_bag) for r in rules])


rules: t.Dict[str, t.Optional[t.List[t.Tuple[str, int]]]] = {}

with open(util.get_input_path(7), "r") as f:
    for line in f.readlines():
        parse_rule(line.strip())
    print(how_many_ancestors("shiny gold"))
