def largestNumber(cost: [int], target: int) -> str:
    l=len(cost)
    a=[]
    s=[]
    for i in range (1,l+1):
        a.append(i)
    print(a)
    print(cost)
    print(sorted(cost,a))
    return 0
    


largestNumber([4,3,2,5,6,7,2,5,5],9)    