import os

import functools as f
import typing as t


T = t.TypeVar('T')


def get_input_path(day: int) -> str:
    dirname = os.path.dirname(os.path.abspath(__file__))
    return f"{dirname}/../inputs/{day}.txt"


def big_intersection(sets: t.List[t.Set[T]]) -> t.Set[T]:
    if sets == []:
        return set()
    return f.reduce(lambda s_1, s_2: s_1.intersection(s_2), sets)


def big_union(sets: t.List[t.Set[T]]) -> t.Set[T]:
    if sets == []:
        return set()
    return f.reduce(lambda s_1, s_2: s_1.union(s_2), sets)
