file = open("input.txt", "r")
rules = file.read().split("\n")

parsed = {}

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


def ric(bag):
    count = 0
    for required, amount in parsed[bag].items():
        count += amount
        count += amount * ric(required)
    return count


result = ric("shiny gold")
print(result)
