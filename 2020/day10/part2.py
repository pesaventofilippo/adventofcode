file = open("input.txt", "r")
lines = file.read().split("\n")

jolts = [int(x) for x in lines]
jolts.sort()
jolts.append(max(jolts) + 3)


cache = {
    0: 1
}
def solve(n):
    if n in jolts:
        if n-1 not in cache:
            cache[n-1] = solve(n-1)
        if n-2 not in cache:
            cache[n-2] = solve(n-2)
        if n-3 not in cache:
            cache[n-3] = solve(n-3)
        return cache[n-1] + cache[n-2] + cache[n-3]
    else:
        return 0

print(solve(max(jolts)))
