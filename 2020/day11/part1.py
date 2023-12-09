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
            for a in range(i-1, i+2):
                for b in range(j-1, j+2):
                    if not (a == i and b == j):
                        if a >= 0 and b >= 0:
                            try:
                                data = seats[a][b]
                                adjacent += data
                            except IndexError:
                                adjacent += "."
                        else:
                            adjacent += "."
            if seat == "L":
                if adjacent.count("#") == 0:
                    newSeats[i][j] = "#"
            elif seat == "#":
                if adjacent.count("#") >= 4:
                    newSeats[i][j] = "L"
    seats = deepcopy(newSeats)
    if newSeats == prevStatus:
        break
    prevStatus = deepcopy(seats)

print(sum([line.count("#") for line in seats]))
