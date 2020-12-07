import util


def count(i: str) -> int:
    return len(set(i.replace("\n", "")))


with open(util.get_input_path(6), "r") as f:
    inp = f.read().strip().split("\n\n")
    print(sum([count(i) for i in inp]))
