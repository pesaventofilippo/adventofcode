file = open("input.txt", "r")
rules = file.read().split("\n")

parsed = {}

def solve(bags, toFind):
    # ritorna lista di bag che contengono toFind
    right = []
    for bag in bags:
        if toFind in parsed[bag]:
            right.append(bag)
    return right


for rule in rules:
    # parsa le regole e crea il dict
    colName = rule.split("contain")[0].replace("bags", "").strip()
    data = rule.split("contain")[1].replace("bags", "").replace("bag", "").replace(".", "").strip()
    otherPacks = data.split(" , ")

    contained = {}
    if otherPacks != ["no other"]:
        for other in otherPacks:
            othName = other.split(" ", 1)[1]
            othNum = int(other.split(" ", 1)[0])
            contained[othName] = othNum

    parsed[colName] = contained


counted = []
def ric(lis, toF):
    count = 0
    res = solve(lis, toF) # quali bag contengono toF
    for b in res:
        if b not in counted:
            counted.append(b)
            count += 1
    for bag in res:
        count += ric(parsed, bag) # i bag che contengono i bag che contengono toF
    return count


result = ric(parsed, "shiny gold")
print(result)
