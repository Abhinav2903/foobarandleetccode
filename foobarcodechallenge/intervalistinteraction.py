def intervalIntersection( A: [[int]], B: [[int]]) -> [[int]]:
    ls=[]
    x=[]
    head=tail=0
    for i in A:
        for j in B:
            if(max(i)>=min(j) and min(i)<=max(j)):
                x=i+j
                # y=sorted(x)
                head=min((max(x[0],x[1]),max(x[1],x[2])))
                tail=min(x[1],x[2])
                ls.append([tail,head])
    return ls

print(intervalIntersection([[0,2],[5,10],[13,23],[24,25]],[[1,5],[8,12],[15,24],[25,26]]))    
# [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]