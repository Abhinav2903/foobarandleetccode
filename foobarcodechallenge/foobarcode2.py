#solution([4, 3, 10, 2, 8], 12)
#solution([1, 2, 3, 4], 15)
def solution(l,t):
    ln= len(l)
    Sum=[]
    my_string = ','.join(map(str, [-1,-1]))
    if(sum(l)>t):
        ##x
        for i in range (0,ln):
            for j in range(1,ln):
                if (sum(l[i:j])==t):
                    Sum.append(sum)
        print(Sum) 
    else:
        print(my_string)       

#solution([1, 2, 3, 4], 15)       
solution([4, 3, 10, 2, 8], 12) 