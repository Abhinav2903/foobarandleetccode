from collections import Counter 
def checkInclusion(s1: str, s2: str) -> bool:
    x1=len(s2)
    x2=len(s1)

    for i in range (0,x1-x2+1):
        j=i+x2
        hk=s2[i:j]
        print(hk)
        
        if(Counter(hk)==Counter(s1)):
            return True
        
        
    

print(checkInclusion("abcdxabcde", "abcdeabcdx"))     

