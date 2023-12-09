import re
file = open("input.txt", "r")

passports = file.read().split("\n\n")
valid = 0
for passport in passports:
    info = re.split(" |\n", passport)
    keys = [pair.split(":")[0] for pair in info]

    if all(x in keys for x in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']):
        valid += 1

print(valid)
