import util
import typing as t


class Computer():

    def __init__(self, program: t.List[t.Tuple[str, int]]):
        self.fptr: int = 0
        self.accumulator: int = 0
        self.seen_insts: t.Set[int] = set()
        self.program: t.List[t.Tuple[str, int]] = program
        self.p_len: int = len(program)

        self.instructions_switch = {
            "nop" : self._nop,
            "acc" : self._acc,
            "jmp" : self._jmp,
        }


    def _acc(self, increment: int) -> None:
        self.accumulator += increment
        self.fptr += 1


    def _jmp(self, x: int) -> None:
        self.fptr += x


    def _nop(self, x: int) -> None:
        self.fptr += 1


    def run(self) -> int:
        while True:
            if self.fptr in self.seen_insts:
                return self.accumulator
            self.seen_insts.add(self.fptr)
            i = self.program[self.fptr]
            self.instructions_switch[i[0]](i[1])


with open(util.get_input_path(8), "r") as f:
    inp: t.List[t.Tuple[str, int]] = [(inst[0], int(inst[1])) for inst in
           [inst.split() for inst in f.readlines()]]
    c = Computer(inp)
    print(c.run())
