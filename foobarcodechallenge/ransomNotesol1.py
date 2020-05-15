def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        mg={i : magazine.count(i) for i in set(magazine)} 
        rN={i : ransomNote.count(i) for i in set(ransomNote)}
        #x=False
        if rN:
            for i in rN:
                if (i in mg and rN[i]<=mg[i]):
                    x=True
                else:
                    x= False
                    break
        elif(rN==mg or not rN):
            x=True
        else:
            x=False        
        return x