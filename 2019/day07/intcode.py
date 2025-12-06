class IntcodeCPU:
    def __init__(self, mem: list[int], inputs: list[int]=None):
        self.ip = 0
        self.mem = mem.copy()
        self.inputs = inputs.copy() if inputs else list()
        self.halted = False

    @classmethod
    def from_line(cls, line: str, inputs: list[int]=None) -> "IntcodeCPU":
        mem = list(map(int, line.split(",")))
        return cls(mem, inputs)

    def add_inputs(self, *inputs: int):
        self.inputs.extend(inputs)

    def _param(self, parameter: int) -> int:
        pmodes = str(self.mem[self.ip])[:-2]
        pmode = pmodes[-parameter] if parameter <= len(pmodes) else "0"
        if pmode == "0":
            return self.mem[self.mem[self.ip + parameter]]
        elif pmode == "1":
            return self.mem[self.ip + parameter]

    def execute_step(self) -> int:
        output = None
        while (not self.halted) and (output is None):
            opcode = self.mem[self.ip] % 100
            match opcode:
                case 99: # HALT
                    self.halted = True
                case 1: # ADD
                    self.mem[self.mem[self.ip+3]] = self._param(1) + self._param(2)
                    self.ip += 4
                case 2: # MUL
                    self.mem[self.mem[self.ip+3]] = self._param(1) * self._param(2)
                    self.ip += 4
                case 3: # INPUT
                    self.mem[self.mem[self.ip+1]] = self.inputs.pop(0)
                    self.ip += 2
                case 4: # OUTPUT
                    output = self._param(1)
                    self.ip += 2
                case 5: # JUMP-IF-TRUE
                    self.ip = self._param(2) if self._param(1) != 0 else self.ip + 3
                case 6: # JUMP-IF-FALSE
                    self.ip = self._param(2) if self._param(1) == 0 else self.ip + 3
                case 7: # LESS THAN
                    self.mem[self.mem[self.ip+3]] = 1 if self._param(1) < self._param(2) else 0
                    self.ip += 4
                case 8: # EQUALS
                    self.mem[self.mem[self.ip+3]] = 1 if self._param(1) == self._param(2) else 0
                    self.ip += 4
        return output

    def execute(self) -> list[int]:
        outputs = list()
        while not self.halted:
            output = self.execute_step()
            if output is not None:
                outputs.append(output)
        return outputs
