file = open("input.txt", "r")
lines = file.read().split("\n")

jolts = [int(x) for x in lines]
jolts.sort()

lastOut = 0
diff_1 = 0
diff_3 = 0
for jolt in jolts:
    diff = jolt - lastOut
    if diff == 1:
        diff_1 += 1
    elif diff == 3:
        diff_3 += 1
    lastOut = jolt

adapter = max(jolts) + 3
diff = adapter - lastOut
if diff == 1:
    diff_1 += 1
elif diff == 3:
    diff_3 += 1

print(diff_1 * diff_3)
