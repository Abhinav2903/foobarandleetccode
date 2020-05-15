def firstUniqChar(s: str) -> int:
    #j=0
    #letters='abcdefghijklmnopqrstuvwxyz'
    #index=[s.index(l) for l in letters if s.count(l) == 1]
    #return min(index) if len(index) > 0 else -1
    for i in s:
        if(s.count(i)==1):
            return j
        j=j+1   
    return -1     
print(firstUniqChar("loveleetcode"))        


