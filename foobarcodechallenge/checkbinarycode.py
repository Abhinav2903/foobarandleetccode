x=[]
def getTheArray(arr, n):
    s=""  
    for i in range(0, n):
        s=s+str(arr[i])
    x.append(s)              
def generatebincode(k,arr,i):
    if (i==k):
        getTheArray(arr,k)
        return arr
    arr[i]=0
    generatebincode(k,arr,i+1)
    arr[i]=1
    generatebincode(k,arr,i+1)
 
def hasAllCodes(s: str, k: int) -> bool:
    arr=[None] * k
    v=0
    generatebincode(k,arr,0)
    print(x) 
    if(k>=len(s) and k>0):
        return False
    else:
        for i in x:
            v=s.count(i)
            if(v==0):
                return False
    return True

print(hasAllCodes("0110",1))    