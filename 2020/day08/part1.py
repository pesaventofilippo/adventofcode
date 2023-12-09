file = open("input.txt", "r")
instructions = file.read().split("\n")

accumulator = 0
pointer = 0
executed = []
while True:
    if pointer not in executed:
        executed.append(pointer)
        ins = instructions[pointer]
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
        print(accumulator)
        break
