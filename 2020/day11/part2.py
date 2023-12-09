from copy import deepcopy
file = open("input.txt", "r")
lines = file.read().split("\n")

seats = []
for line in lines:
    seats.append(list(line))

prevStatus = seats
while True:
    newSeats = deepcopy(seats)
    for i in range(len(seats)):
        for j in range(len(seats[i])):
            seat = seats[i][j]
            adjacent = ""
            for dir in ["u", "d", "l", "r", "ul", "ur", "dl", "dr"]:
                reachedEnd = False
                found = "."
                x = i
                y = j
                while found == "." and not reachedEnd:
                    if dir == "u":
                        x -= 1
                    elif dir == "d":
                        x += 1
                    elif dir == "l":
                        y -= 1
                    elif dir == "r":
                        y += 1
                    elif dir == "ul":
                        x -= 1
                        y -= 1
                    elif dir == "ur":
                        x -= 1
                        y += 1
                    elif dir == "dl":
                        x += 1
                        y -= 1
                    elif dir == "dr":
                        x += 1
                        y += 1

                    if x >= 0 and y >= 0:
                        try:
                            data = seats[x][y]
                            found = data
                        except IndexError:
                            reachedEnd = True
                    else:
                        reachedEnd = True
                adjacent += found

            if seat == "L":
                if adjacent.count("#") == 0:
                    newSeats[i][j] = "#"
            elif seat == "#":
                if adjacent.count("#") >= 5:
                    newSeats[i][j] = "L"
    seats = deepcopy(newSeats)
    if newSeats == prevStatus:
        break
    prevStatus = deepcopy(seats)

print(sum([line.count("#") for line in seats]))
