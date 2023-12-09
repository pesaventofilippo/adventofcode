file = open("input.txt", "r")
lines = file.read().split("\n")

numbers = [int(x) for x in lines]
start = 0
while start < len(numbers)-25:
    found = False
    for i in range(start, start+25):
        for j in range(start, start+25):
            if numbers[i] != numbers[j]:
                res = numbers[i] + numbers[j]
                if res == numbers[start+25]:
                    found = True
    if not found:
        print(numbers[start+25])
        break
    else:
        start += 1
