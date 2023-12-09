TIME = 45988373
RECORD = 295173412781210

ways = 0
for starttime in range(TIME):
    start_vel = starttime
    race_time = TIME - starttime
    distance = start_vel * race_time
    if distance >= RECORD:
        ways += 1

print(ways)
