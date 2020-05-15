#from ordered_set import OrderedSet
#from ordered_set import OrderedSet
def removeKdigits(num, k) -> str:
    op=[]
    if(k==0):
        return num
    elif(k==len(num)):
        return 0
    else:
        for i in num:
            while(k>0  and len(op)>0 and op[-1]>i):
                k=k-1
                op.pop()
            op.append(i)
    if(k>0):
        op = op[:-k]
        ans=''.join(op)
        Ans=int(ans)
        ans=str(Ans)
        
        #return(ans.lstrip('0'))
    else:
        ans=''.join(op)
        Ans=int(ans)
        ans=str(Ans)
        
        #return(ans.lstrip('0'))
    return ans    
    
print(removeKdigits("10200",2))    