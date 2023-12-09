file = open("input.txt", "r")
lines = file.read().split("\n")

time = int(lines[0])
buses = [int(x) for x in lines[1].split(",") if x != "x"]
waits = []

for bus in buses:
    dep = 0
    while dep < time:
        dep += bus
    waits.append(dep)

waitTime = min(waits) - time
busId = buses[waits.index(min(waits))]
print(busId * waitTime)
