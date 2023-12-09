file = open("input.txt", "r")
rows = file.read().split("\n")

trees = 0
row = 0
col = 0
while row < len(rows):
    pos = rows[row][col]
    if pos == "#":
        trees += 1
    col += 1 # right 3
    row += 2 # down 1
    if row < len(rows):
        if not col < len(rows[row]):
            col -= len(rows[row])

print(trees)
