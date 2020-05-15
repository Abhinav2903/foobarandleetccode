

def majorityElement(nums):
    n=len(nums)
    n=n//2
    nums.sort()
    max=nums[n]
    return max
        
M = majorityElement([1])
print(M)