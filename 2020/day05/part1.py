file = open("input.txt", "r")
lines = file.read().split("\n")

results = []
for ins in lines:
    first = ins[:7]
    second = ins[7:]

    first_bin = "".join(["0" if x == "F" else "1" for x in first])
    second_bin = "".join(["0" if x == "L" else "1" for x in second])

    row = int(first_bin, 2)
    col = int(second_bin, 2)
    seat_id = row*8 + col
    results.append(seat_id)

print(max(results))
