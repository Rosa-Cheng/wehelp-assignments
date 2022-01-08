def maxZeros(nums):
    if not nums:
        return 0
    counter = 0
    result = 0
    for index in range(len(nums)):
        if nums[index] == 0:
            counter += 1
            result = max(result, counter)
        else:
            counter = 0
    print(result)
maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0
maxZeros([0, 0, 0, 1, 1]) # 得到 3