import re
file = open("input.txt", "r")

passports = file.read().split("\n\n")
valid = 0
for passport in passports:
    info = re.split(" |\n", passport)
    passInfo = {}
    for pair in info:
        dataSplit = pair.split(":")
        passInfo[str(dataSplit[0])] = str(dataSplit[1])

    checks = 0
    if all(x in passInfo.keys() for x in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']):
        try:
            byear = int(passInfo["byr"])
        except ValueError:
            continue
        if 1920 <= byear <= 2002:
            checks += 1

        try:
            iyear = int(passInfo["iyr"])
        except ValueError:
            continue
        if 2010 <= iyear <= 2020:
            checks += 1

        try:
            eyear = int(passInfo["eyr"])
        except ValueError:
            continue
        if 2020 <= eyear <= 2030:
            checks += 1

        if passInfo["hgt"].endswith("in"):
            try:
                height = int(passInfo["hgt"][:-2])
            except ValueError:
                continue
            if 59 <= height <= 76:
                checks += 1
        elif passInfo["hgt"].endswith("cm"):
            try:
                height = int(passInfo["hgt"][:-2])
            except ValueError:
                continue
            if 150 <= height <= 193:
                checks += 1

        if passInfo["hcl"].startswith("#") and len(passInfo["hcl"]) == 7:
            chars = passInfo["hcl"][1:]
            chco = 0
            for c in chars:
                if '0' <= c <= '9' or 'a' <= c <= 'f':
                    chco += 1
            if chco == 6:
                checks += 1

        if passInfo["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            checks += 1

        if len(passInfo["pid"]) == 9:
            try:
                _ = int(passInfo["pid"])
            except ValueError:
                continue
            checks += 1

    if checks == 7:
        valid += 1

print(valid)
