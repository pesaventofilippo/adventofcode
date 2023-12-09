file = open("input.txt", "r")
nums = [int(x) for x in file.read().split("\n")]

for i in range(len(nums)):
    for j in range(len(nums)):
        for k in range(len(nums)):
            if (i != j) and (i != k) and (j != k):
                if nums[i] + nums[j] + nums[k] == 2020:
                    print(nums[i] * nums[j] * nums[k])
