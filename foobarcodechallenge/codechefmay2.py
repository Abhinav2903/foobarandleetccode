def chef():
    
    t=int(input())
    ans=[]
    while(t):
        N,Q=map(int, input().split())
        
        S=input()
        ns=set(S)
        q=[]
        count=0
        for i in range(Q):
           IP=int(input()) 
           q.append(IP)
        for i in q:
            for j in ns:
                if(S.count(j)>i):
                    count=count+S.count(j)-1
            ans.append(count)
            count=0   
        t=t-1

    
        print(ans)
chef()
#stayinghomesaveslife