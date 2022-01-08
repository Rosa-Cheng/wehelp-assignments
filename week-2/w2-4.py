def twoSum(nums, target):
    numMap = {}
    for i in range(len(nums)):
        if numMap.__contains__(target-nums[i]):
            return [numMap.get(target-nums[i]), i]
        else:
            numMap[nums[i]] = i
result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9