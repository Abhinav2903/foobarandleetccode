def solution(l):
    a=[]
    x=0
    for j in range(len(l)):
        a.append(l[j])
    #here lamda function convert string to int and return as list 
    L=lambda s: list(map(int, s.split('.')))
    for i in l:
        a[x]=L(i)
        x=x+1
    # gere we sort the list and after for loop a values are changed
    a.sort()
    print(a)
    
    # sort function is quiet handy as it does not change values of the list it just sort according the function given as we have given lamda
    l.sort(key=lambda  s: list(map(int, s.split('.'))))
    #print(",".join(a))
    #l.sor
    #t((lambda x: list(map(int, x.split('.')))))
    print(l)
    #print(",".join(l))   
    
solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"])  


















#0.1,1.1.1,1.2,1.2.1,1.11,2,2.0,2.0.0
#new=sorted(x)
    #for i in zero:
	#    for j in range (0,lt):
	#	    y.append(new[j].replace(i,"."))
    

    #print (', '.join(l)) 
    #print(l)