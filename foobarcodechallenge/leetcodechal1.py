def maxPower(s) -> int:
    ns=set(s)
    maxp=[]
    prevs=""
    c=prevc=1
    
    for i in ns:
        maxp.append(s.count(i))
    
    for j in s:
       if(prevs==j):
           c+=1
           if(prevc<c):
                prevc=c
        
       else:
            c=1    
       prevs=j
    return prevc

    # print(maxp)
    # print(ns)       


print(maxPower(""))        


