file = open("input.txt", "r")
instructions = file.read().split("\n")


def execute(code):
    accumulator = 0
    pointer = 0
    executed = []
    while True:
        if pointer not in executed:
            executed.append(pointer)
            if pointer < len(code):
                ins = code[pointer]
                txt = ins.split(" ")[0]
                val = int(ins.split(" ")[1])

                if txt == "acc":
                    accumulator += val
                elif txt == "jmp":
                    pointer += val - 1
                elif txt == "nop":
                    pass

                pointer += 1
            else:
                return accumulator
        else:
            raise RuntimeError


for pointer in range(len(instructions)):
    insCopy = instructions.copy()
    ins = insCopy[pointer]
    if ins.startswith("jmp"):
        insCopy[pointer] = ins.replace("jmp", "nop")
    elif ins.startswith("nop"):
        insCopy[pointer] = ins.replace("nop", "jmp")

    try:
        res = execute(insCopy)
        print(res)
    except RuntimeError:
        continue
