file = open("input.txt", "r")
groups = file.read().split("\n\n")

total = 0
for group in groups:
    answered = []
    people = group.split("\n")
    for p in people:
        for ans in p:
            if ans not in answered:
                answered.append(ans)
    total += len(answered)

print(total)
