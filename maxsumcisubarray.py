def maxSubarraySumCircular(A):
    total, maxSum, curMax, minSum, curMin = 0, -float('inf'), 0,float('inf'),0
    for i in A:
        curMax=max(curMax+i,i)
        curMin =min(curMin+i,i)
        maxSum=max(maxSum,curMax)
        minSum=min(minSum,curMin)
        total+=i
    return max(maxSum,total-minSum) if maxSum >0 else maxSum

print(maxSubarraySumCircular([-1,-2,-3]))      

