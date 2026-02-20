def permute(nums):
    n = len(nums)
    res = []
    def helper(index):
        if index == n-1:
            res.append(nums[:])
        for j in range(index,x):
            nums[index],nums[j] = nums[j],nums[index]
            helper(index+1)
            nums[index],nums[j] = nums[j],nums[index]
    helper(0)
    return res

nums = [1,2,3]
print(permute(nums))