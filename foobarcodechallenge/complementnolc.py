def findComplement(num: int) -> int:
        rc=[]
        N=k=0
        while(num):
            R=num%2
            if(R==1):
                rc.append(0)
            else:
                rc.append(1)    
            num=num//2 
        for j in rc:
            N=N+j*pow(2,k)
            k=k+1
        return N

print(findComplement(7))

def findCompBybin(num: int) -> int:
    k=o=0
    b=bin(num).replace("0b","")
    for j in b[::-1]:
        if(j=="1"):
            o=o+0*pow(2,k)
        else:
            o=o+1*pow(2,k)    
        k+=1
    return o
print(findCompBybin(7))    


def comp(num: int)->int:
     x=2**(len(bin(num)[2:]))
     y=x-1

     return num^(y)


print(comp(7))     