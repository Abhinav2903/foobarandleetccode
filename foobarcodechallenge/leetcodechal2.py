from fractions import Fraction
def simplifiedFractions(n: int) -> [str]:
    s=[]
    j=1
    if(n==1):
        return s
    while(j%n!=0):
        for i in range (j,n+1):
            x=str(Fraction(j,i))
            if(x!="1"):
                s.append(x)
        j=j+1
    y=sorted(list(set(s)))

    return y
print(simplifiedFractions(4))    