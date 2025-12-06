def execute(mem: list[int], inputs: list[int]) -> list[int]:
    def read(parameter: int) -> list[int]:
        pmodes = str(mem[ip])[:-2]
        pmode = pmodes[-parameter] if parameter <= len(pmodes) else "0"
        if pmode == "0":
            return mem[mem[ip + parameter]]
        elif pmode == "1":
            return mem[ip + parameter]

    mem = mem.copy()
    ip = 0

    while True:
        opcode = mem[ip] % 100
        if opcode == 99: # HALT
            break
        if opcode == 1: # ADD
            mem[mem[ip+3]] = read(1) + read(2)
            ip += 4
        elif opcode == 2: # MUL
            mem[mem[ip+3]] = read(1) * read(2)
            ip += 4
        elif opcode == 3: # INPUT
            mem[mem[ip+1]] = inputs.pop(0)
            ip += 2
        elif opcode == 4: # OUTPUT
            print(read(1))
            ip += 2
        elif opcode == 5: # JUMP-IF-TRUE
            ip = read(2) if read(1) != 0 else ip + 3
        elif opcode == 6: # JUMP-IF-FALSE
            ip = read(2) if read(1) == 0 else ip + 3
        elif opcode == 7: # LESS THAN
            mem[mem[ip+3]] = 1 if read(1) < read(2) else 0
            ip += 4
        elif opcode == 8: # EQUALS
            mem[mem[ip+3]] = 1 if read(1) == read(2) else 0
            ip += 4

    return mem
