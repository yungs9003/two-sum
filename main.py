def twoSum(nums, target):
    a = len(nums)
    b = 0
    c = []
    for i in range (1,a):
        for j in range (0,i):
            if nums[j]+nums[i]=target:
                c.append(i)
                c.append(j)
                b=1
                break
        if b==1:
            break
    return c  

