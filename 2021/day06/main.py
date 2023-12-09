def simulate(days):
    with open("input.txt") as file:
        start = [int(x) for x in file.readline().split(",")]
        fishes = [start.count(i) for i in range(9)]

    for _ in range(days):
        babies = fishes[0]
        for i in range(8):
            fishes[i] = fishes[i+1]
        fishes[6] += babies
        fishes[8] = babies

    return sum(fishes)

print(simulate(80))
print(simulate(256))
