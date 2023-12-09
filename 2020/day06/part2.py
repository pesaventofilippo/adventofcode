file = open("input.txt", "r")
groups = file.read().split("\n\n")

total = 0
for group in groups:
    answered = {}
    people = group.split("\n")
    for p in people:
        for ans in p:
            if not ans in answered:
                answered[ans] = 1
            else:
                answered[ans] += 1

    for val in answered.values():
        if val == len(people):
            total += 1

print(total)
