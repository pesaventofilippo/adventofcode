file = open("input.txt", "r")
lines = file.read().split("\n")

seatIds = []
for ins in lines:
    first = ins[:7]
    second = ins[7:]

    first_bin = "".join(["0" if x == "F" else "1" for x in first])
    second_bin = "".join(["0" if x == "L" else "1" for x in second])

    row = int(first_bin, 2)
    col = int(second_bin, 2)

    seat_id = row*8 + col
    seatIds.append(seat_id)

seatIds.sort()
for seat in seatIds:
    index = seatIds.index(seat)
    if 0 < index < len(seatIds)-1:
        if seatIds[index+1] == seat+2:
            print(seat+1)
