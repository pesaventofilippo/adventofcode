file = open("input.txt", "r")
lines = file.read().split("\n")

numbers = [int(x) for x in lines]
start = 0
token = -1
while start < len(numbers)-25:
    found = False
    for i in range(start, start+25):
        for j in range(start, start+25):
            if numbers[i] != numbers[j]:
                res = numbers[i] + numbers[j]
                if res == numbers[start+25]:
                    found = True
    if not found:
        token = numbers[start+25]
        break
    else:
        start += 1

elements = []
pointer = 0
while sum(elements) != token:
    if sum(elements) < token:
        elements.append(numbers[pointer])
        pointer += 1
    elif sum(elements) > token:
        elements = elements[1:]

print(min(elements) + max(elements))
