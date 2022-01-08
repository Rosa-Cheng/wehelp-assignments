def maxProduct(nums):
    a=len(nums)
    max = nums[0]*nums[1]
    for x in range(a):
        for y in range(x+1,a):
            maxf = nums[x]*nums[y]
            if maxf>max:
                max=maxf
    print(max)
maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([-1, -2, 0]) # 得到 2