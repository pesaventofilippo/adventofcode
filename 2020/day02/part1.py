file = open("input.txt", "r")
lines = file.read().split("\n")

valid = 0
for line in lines:
    data = line.split()
    let_min = int(data[0].split("-")[0])
    let_max = int(data[0].split("-")[1])
    lett = data[1].replace(":", "")
    password = data[2]

    if let_min <= password.count(lett) <= let_max:
        valid += 1

print(valid)
