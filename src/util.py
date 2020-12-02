import os

import typing as t


def get_input_path(day: int) -> str:
    dirname = os.path.dirname(os.path.abspath(__file__))
    return f"{dirname}/../inputs/{day}.txt"
