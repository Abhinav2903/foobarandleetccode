def twoCitySchedCost(costs: [[int]]) -> int:
    sum=0
    sorted_cost=sorted(costs,key=lambda x: x[0]-x[1])
    for i in range(len(costs)):
        if(i<len(costs)//2):
            sum+=sorted_cost[i][0]
        else:
            sum+=sorted_cost[i][1]    
    return sum


print(twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]]))
