
class Solution:
    def singleNonDuplicate(self,nums) -> int:
        self.l=len(nums)    
        if(self.l>1):
            L=self.l
            mid=int(L/2)+1
        #print(mid)
            if(mid%2!=0):
                newarr=nums[0:mid]
            else:
                newarr=nums[mid:self.l]
                if(mid==2):
                    a=nums[0:1]
                    b=nums[1:self.l]
                    B=b[0]+b[1]
                    if(B/b[0]==2):
                        return a[0]
                    else:
                        return b[1]    

            return self.singleNonDuplicate(newarr)
        else:
            return nums[0]
                    
s=Solution()    
print(s.singleNonDuplicate([1,1,2,2,3]))
#soltype 1 using len function it takes uch time
# soltype2 for only if all element accur twice and single element occur 1 then we can use sets 
# with this sol return sum(set(nums))*2-sum(nums)
# sol 3 for sorted array using recursive binary search with mid value here given my solution in this code   
# which is not woring but the hint given below
# use mid and nums[i]==nums[i+1] for every even i change mid accordingly 
# for mire got to leetcode submission this sol id for logn complexity 
# all other prev sol are also rite but not for logn they have much more time complexity          