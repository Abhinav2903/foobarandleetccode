import math
def isPerfectSquare(num: int) -> bool:
    x=math.sqrt(num)
    y=math.ceil(x)
    z=pow(y,2)
    a=(num-z)
    if(a==0):
        return True
    return False    

print(isPerfectSquare(24))    