file = open("input.txt", "r")
lines = file.read().split("\n")

valid = 0
for line in lines:
    data = line.split()
    pos_1 = int(data[0].split("-")[0])
    pos_2 = int(data[0].split("-")[1])
    lett = data[1].replace(":", "")
    password = data[2]

    if ((password[pos_1-1] == lett) and (password[pos_2-1] != lett)) \
        or ((password[pos_1-1] != lett) and (password[pos_2-1] == lett)):
        valid += 1

print(valid)
