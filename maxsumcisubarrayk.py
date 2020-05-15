def kaden(a):
    curr_max=float('-inf') #initialize with minimest of number
    max_ending=0           
    for i in a:
        max_ending=i+max_ending # edit max ending
        if(max_ending<0):       # by using this if conddition we just discard prev contiguos negative numbers 
            max_ending=0        # here we come if we got more negatives in path way than positive
        if(curr_max<max_ending): #we can only go if the new number of contiguoas sum is greater than prev stored
            curr_max=max_ending  # eg currmax=1,maxend=2 then after that currmax=2  
    return curr_max   

def maxSubarraySumCircular(a):
    allnegative=False
    l=0
    for i in a:          #check for all negative
        if(i<0):
            l=l+1
        else:
            allnegative=False
            break
        allnegative=True
    if(allnegative==True):
        return max(a)
    else:

        maxa=kaden(a) #max sub array sum of a
    #tsum=sum(a)
        ttsum=0
        for i in range (len(a)):
            ttsum=ttsum+a[i]         #here we are calculating total sum
            a[i]=-a[i]               #here we are inverting the values a

        maxi= kaden(a)              #here we are getting inverted array kaden means max negative contiguas sum
        maxi=maxi+ttsum             #updating maxi to kind of total maxi

        if(maxi>maxa):
            print("maxi")
            return maxi
        else:
            print("kaden")
            return maxa    


#print(kaden([1,2,-3]))
print(maxSubarraySumCircular([-2,-3,-1]))    