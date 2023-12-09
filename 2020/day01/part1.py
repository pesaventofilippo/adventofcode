file = open("input.txt", "r")
nums = [int(x) for x in file.read().split("\n")]

for i in range(len(nums)):
    for j in range(len(nums)):
        if (i != j) and (nums[i] + nums[j] == 2020):
            print(nums[i] * nums[j])
