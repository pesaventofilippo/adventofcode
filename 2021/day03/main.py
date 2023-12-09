def first(input):
    gamma = ""
    epsilon = ""
    for i in range(len(input[0])):
        bits = [b[i] for b in input]
        if bits.count("1") > bits.count("0"):
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    return int(gamma, 2) * int(epsilon, 2)


def second(input):
    oxy = ""
    co2 = ""
    for i in range(len(input[0])):
        oxyBits = [b[i] for b in input if b.startswith(oxy)]
        co2Bits = [b[i] for b in input if b.startswith(co2)]

        if len(oxyBits) > 1:
            oxy += "1" if oxyBits.count("1") >= oxyBits.count("0") else "0"
        else:
            oxy += oxyBits[0]

        if len(co2Bits) > 1:
            co2 += "0" if co2Bits.count("1") >= co2Bits.count("0") else "1"
        else:
            co2 += co2Bits[0]

    return int(oxy, 2) * int(co2, 2)


with open("input.txt") as f:
    bytes = [l.strip() for l in f.readlines()]
    print(first(bytes))
    print(second(bytes))
