def mincostClimbingStairs(cost):
    n = len(cost)
    def helper(index):
        # return the min cost for reaching the top starting from step-index
        #base 
        if index > n-1: return 0
        #recursive case 
        onestep = cost[index] + helper(index+1)
        #two step 
        twostep = cost[index] + helper(index+2)
        return min(onestep,twostep)
    return min(helper(0),helper(1))