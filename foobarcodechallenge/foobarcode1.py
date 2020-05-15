def solution(data, n): 
    # Your code here
    cnt = []
    for i in data:
        if(data.count(i)>n):  # count occurence of i in list
            cnt.append(i)
            
    for j in cnt:
        data.remove(j)       # remove desired element from list
    my_string = ','.join(map(str, data)) #for conversion to comma seprated string from list 
    print(my_string)
    #print (*data,sep=",")
    #print (data)
#solution([1, 2, 3], 0)
solution([1, 2, 2, 3, 3, 3, 4, 5, 5], 0)    