class IntcodeCPU:
    def __init__(self, mem: dict[int, int], inputs: list[int]=None):
        self.ip = 0
        self.base = 0
        self.mem = mem.copy()
        self.inputs = inputs.copy() if inputs else list()
        self.halted = False

    @classmethod
    def from_line(cls, line: str, inputs: list[int]=None) -> "IntcodeCPU":
        mem = list(map(int, line.split(",")))
        mem = {i: v for i, v in enumerate(mem)}
        return cls(mem, inputs)

    def add_inputs(self, *inputs: int):
        self.inputs.extend(inputs)

    def memread(self, addr: int) -> int:
        return self.mem.get(addr, 0)

    def memwrite(self, addr: int, value: int):
        self.mem[addr] = value

    def param_addr(self, parameter: int) -> int:
        pmodes = str(self.memread(self.ip))[:-2]
        pmode = pmodes[-parameter] if parameter <= len(pmodes) else "0"
        if pmode == "0": # POSITION
            return self.memread(self.ip + parameter)
        elif pmode == "1": # IMMEDIATE
            return self.ip + parameter
        elif pmode == "2": # RELATIVE
            return self.base + self.memread(self.ip + parameter)

    def param(self, parameter: int) -> int:
        return self.memread(self.param_addr(parameter))

    def execute_step(self) -> int:
        output = None
        while (not self.halted) and (output is None):
            opcode = self.memread(self.ip) % 100
            match opcode:
                case 99: # HALT
                    self.halted = True
                case 1: # ADD
                    res = self.param(1) + self.param(2)
                    self.memwrite(self.param_addr(3), res)
                    self.ip += 4
                case 2: # MUL
                    res = self.param(1) * self.param(2)
                    self.memwrite(self.param_addr(3), res)
                    self.ip += 4
                case 3: # INPUT
                    res = self.inputs.pop(0)
                    self.memwrite(self.param_addr(1), res)
                    self.ip += 2
                case 4: # OUTPUT
                    output = self.param(1)
                    self.ip += 2
                case 5: # JUMP-IF-TRUE
                    self.ip = self.param(2) if self.param(1) != 0 else self.ip + 3
                case 6: # JUMP-IF-FALSE
                    self.ip = self.param(2) if self.param(1) == 0 else self.ip + 3
                case 7: # LESS THAN
                    res = 1 if self.param(1) < self.param(2) else 0
                    self.memwrite(self.param_addr(3), res)
                    self.ip += 4
                case 8: # EQUALS
                    res = 1 if self.param(1) == self.param(2) else 0
                    self.memwrite(self.param_addr(3), res)
                    self.ip += 4
                case 9: # RELATIVE BASE OFFSET
                    self.base += self.param(1)
                    self.ip += 2
        return output

    def execute(self) -> list[int]:
        outputs = list()
        while not self.halted:
            output = self.execute_step()
            if output is not None:
                outputs.append(output)
        return outputs
