def execute(mem: list[int]) -> list[int]:
    mem = mem.copy()
    ip = 0
    while mem[ip] != 99:
        if mem[ip] == 1:
            mem[mem[ip + 3]] = mem[mem[ip + 1]] + mem[mem[ip + 2]]
        elif mem[ip] == 2:
            mem[mem[ip + 3]] = mem[mem[ip + 1]] * mem[mem[ip + 2]]
        ip += 4
    return mem
