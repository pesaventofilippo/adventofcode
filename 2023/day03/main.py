SYMBOLS = {'@', '&', '/', '$', '+', '-', '*', '%', '#', '='}
matrix = []


def scan_numbers(i: int, j: int) -> int:
    if (i < 0) or (j < 0) or (i >= len(matrix)) or (j >= len(matrix[i])):
        return None
    if not matrix[i][j].isdigit():
        return None

    current_num = str(matrix[i][j])
    matrix[i][j] = '.'

    scan_j = j-1
    while scan_j >=0 and matrix[i][scan_j].isdigit():
        current_num = str(matrix[i][scan_j]) + current_num
        matrix[i][scan_j] = '.'
        scan_j -= 1

    scan_j = j+1
    while scan_j < len(matrix[i]) and matrix[i][scan_j].isdigit():
        current_num += str(matrix[i][scan_j])
        matrix[i][scan_j] = '.'
        scan_j += 1

    return int(current_num)


with open("input.txt") as f:
    for line in f.readlines():
        line = line.strip()
        matrix.append([c for c in line])


total = 0
for i, row in enumerate(matrix):
    for j, c in enumerate(row):
        if c  == '*':
            numbers = [
                scan_numbers(i-1, j-1),
                scan_numbers(i-1, j),
                scan_numbers(i-1, j+1),

                scan_numbers(i, j-1),
                scan_numbers(i, j+1),

                scan_numbers(i+1, j-1),
                scan_numbers(i+1, j),
                scan_numbers(i+1, j+1)
            ]
            numbers = [n for n in numbers if n]
            if len(numbers) == 2:
                total += numbers[0] * numbers[1]

print(total)
