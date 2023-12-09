def tableWin(table):
    for row in table:
        if all([cell[1] for cell in row]):
            return True

    for col in range(len(table[0])):
        if all([row[col][1] for row in table]):
            return True

    return False

def first():
    with open("input.txt") as f:
        pool = [int(x) for x in f.readline().strip().split(",")]
        tables = []
        while f.readline():
            table = []
            for _ in range(5):
                row = [[int(x), False] for x in f.readline().strip().split()]
                table.append(row)
            tables.append(table)

    extracted = None
    while not any([tableWin(table) for table in tables]):
        extracted = pool.pop(0)
        for table in tables:
            for row in table:
                for cell in row:
                    if cell[0] == extracted:
                        cell[1] = True

    winner = None
    for table in tables:
        if tableWin(table):
            winner = table
            break

    score = sum([cell[0] for row in winner for cell in row if not cell[1]])
    return score * extracted


def second():
    with open("input.txt") as f:
        pool = [int(x) for x in f.readline().strip().split(",")]
        tables = []
        while f.readline():
            table = []
            for _ in range(5):
                row = [[int(x), False] for x in f.readline().strip().split()]
                table.append(row)
            tables.append(table)

    lastExtracted = None
    lastWinner = None
    while len(pool) > 0:
        extracted = pool.pop(0)
        i = 0
        while i < len(tables):
            table = tables[i]
            for row in table:
                for cell in row:
                    if cell[0] == extracted:
                        cell[1] = True

            if tableWin(table):
                lastWinner = table
                lastExtracted = extracted
                tables.remove(table)
                i -= 1
            i += 1

    score = sum([cell[0] for row in lastWinner for cell in row if not cell[1]])
    return score * lastExtracted


print(first())
print(second())
