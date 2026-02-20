def subsets(nums):
    res = []
    def helper(nums,i,subset):
        if i == len(nums):
            res.append(subset.copy())
            return
        helper(nums,i+1,subset)
        subset.append(nums[i])
        helper(nums,i+1,subset)
        subset.pop()
    helper(nums,0,[])
    return res
print(subsets([1,2,3]))