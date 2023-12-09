def first(input):
    vents = []
    for line in input:
        p1, p2 = line.split(" -> ")
        x1, y1 = [int(x) for x in p1.split(",")]
        x2, y2 = [int(x) for x in p2.split(",")]
        vents.append(
            ((x1, y1), (x2, y2))
        )

    max_x1 = max(vents, key=lambda x: x[0][0])[0][0]
    max_y1 = max(vents, key=lambda x: x[0][1])[0][1]
    max_x2 = max(vents, key=lambda x: x[1][0])[1][0]
    max_y2 = max(vents, key=lambda x: x[1][1])[1][1]
    max_x = max(max_x1, max_x2)
    max_y = max(max_y1, max_y2)

    table = []
    for _ in range(max_x + 1):
        row = []
        for _ in range(max_y + 1):
            row.append(0)
        table.append(row)

    for (x1, y1), (x2, y2) in vents:
        if x1 == x2:
            for y in range(min(y1,y2), max(y1,y2) + 1):
                table[x1][y] += 1
        elif y1 == y2:
            for x in range(min(x1,x2), max(x1,x2) + 1):
                table[x][y1] += 1

    count = 0
    for row in table:
        for cell in row:
            if cell > 1:
                count += 1

    return count


def second(input):
    vents = []
    for line in input:
        p1, p2 = line.split(" -> ")
        x1, y1 = [int(x) for x in p1.split(",")]
        x2, y2 = [int(x) for x in p2.split(",")]
        vents.append(
            ((x1, y1), (x2, y2))
        )

    max_x1 = max(vents, key=lambda x: x[0][0])[0][0]
    max_y1 = max(vents, key=lambda x: x[0][1])[0][1]
    max_x2 = max(vents, key=lambda x: x[1][0])[1][0]
    max_y2 = max(vents, key=lambda x: x[1][1])[1][1]
    max_x = max(max_x1, max_x2)
    max_y = max(max_y1, max_y2)

    table = []
    for _ in range(max_x + 1):
        row = []
        for _ in range(max_y + 1):
            row.append(0)
        table.append(row)

    for (x1, y1), (x2, y2) in vents:
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                table[x1][y] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                table[x][y1] += 1
        else:
            incX = 1 if x1 < x2 else -1
            incY = 1 if y1 < y2 else -1
            x = x1
            y = y1
            table[x][y] += 1
            while x != x2 or y != y2:
                x += incX
                y += incY
                table[x][y] += 1

    count = 0
    for row in table:
        for cell in row:
            if cell > 1:
                count += 1

    return count


with open("input.txt") as f:
    data = f.readlines()
    print(first(data))
    print(second(data))
