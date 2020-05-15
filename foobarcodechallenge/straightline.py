def checkStraightLine(coordinates) -> bool:
    l=len(coordinates)
    x1=coordinates[0][0]
    y1=coordinates[0][1]
    x2=coordinates[1][0]
    y2=coordinates[1][1]
    if(l==2):
        return True

    else:
        if(x2==x1):
            for i in coordinates[2:l]:
                if i[0] != x1:
                    return False
            return True

        elif(y2==y1):
            for i in coordinates[2:l]:
                if i[1]!=y1:
                    return False
            return True
        else:                    
            for i in coordinates[2:l]:
                m=(y2-y1)/(x2-x1)
                a=(m*i[0]-i[1]-(m*x1)+y1)
                if(a==0):
                    l=l-1
                else:
                    return False
            return True              

print(checkStraightLine([[-7,-3],[-7,-1],[-2,-2],[0,-8],[2,-2],[5,-6],[5,-5],[1,7]]))