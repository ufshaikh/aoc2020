import re
import util

fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}


def _byr(content):
    try:
        i = int(content)
        return 1920 <= i <= 2002
    except:
        return False


def _iyr(content):
    try:
        i = int(content)
        return 2010 <= i <= 2020
    except:
        return False


def _eyr(content):
    try:
        i = int(content)
        return 2020 <= i <= 2030
    except ValueError:
        return False


def _hgt(content):
    try:
        i = int(re.search(r"^\d+(?=(cm$|in$))", content).group())
        u = content[-2:]
        if u == "cm":
            return 150 <= i <= 193
        elif u == "in":
            return 50 <= i <= 76
        return False
    except (ValueError, AttributeError):
        return False


def _hcl(content):
    if not content[0] == "#" or len(content) != 7:
        return False
    content = "0x" + content[1:]
    try:
        int(content, 0)
        return True
    except ValueError:
        return False


def _ecl(content):
    return content in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}


def _pid(content):
    try:
        int(content)
        return len(content) == 9
    except ValueError:
        return False


validity_switch = {
    "byr": _byr,
    "iyr": _iyr,
    "eyr": _eyr,
    "hgt": _hgt,
    "hcl": _hcl,
    "ecl": _ecl,
    "pid": _pid,
    "cid": lambda x: True,
}


def is_valid_p(p):
    es = {e[0]: e[1] for e in map(lambda x: x.split(":"), p.split())}
    seen_es = set(es.keys())
    return (len(fields - seen_es) == 0
            and all([validity_switch[e](es[e]) for e in es]))


with open(util.get_input_path(4), "r") as f:
    ps = f.read().split("\n\n")
    print(sum(map(is_valid_p, ps)))
