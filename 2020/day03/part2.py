file = open("input.txt", "r")
rows = file.read().split("\n")
slopes = [
    [1, 1],
    [3, 1],
    [5, 1],
    [7, 1],
    [1, 2]
]

total = 1
for slope in slopes:
    trees = 0
    row = 0
    col = 0
    while row < len(rows):
        pos = rows[row][col]
        if pos == "#":
            trees += 1
        col += slope[0]
        row += slope[1]
        if row < len(rows):
            if not col < len(rows[row]):
                col -= len(rows[row])
    total *= trees

print(total)
