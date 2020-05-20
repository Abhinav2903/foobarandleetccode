def busyStudent(startTime: [int], endTime: [int], queryTime: int) -> int:
    a=[]
    c=0
    for i in range (0,len(startTime)):
        x=startTime[i]
        y=endTime[i]
        if(x<=queryTime and y>=queryTime):
            c+=1
        
    return c

print(busyStudent( [1,1,1,1],[1,3,2,4], 7))    


     