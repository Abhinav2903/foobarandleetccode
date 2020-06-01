def findMaxLength(nums: [int]) -> int:
    a=[]
    s=0
    ps=0
    l=0
    while(nums):
        # s=nums[c]+nums[c+1]
        # if(s==1 and s!=ps):
            # l+=2
        x=nums    
        if(len(nums)%2==0):
            if(sum(nums)==len(nums)//2):
                return len(nums)
            else:
                nums.pop()
                nums.pop()


        # if len(a)==0:
            # a.append(c)
        # else:
            # if(prev!=i):
                # a.append(c)
                # cnt=len(a)
            # else:
                # cnt=len(a)
                # a.clear()
        # if(cnt>pcnt):
            # pcnt=cnt 
        # prev=i            
    return l

print(findMaxLength([0,0,0,1,1,0]))