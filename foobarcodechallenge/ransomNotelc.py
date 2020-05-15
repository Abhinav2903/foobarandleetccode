
###
#print(canConstruct("",""))            
#Input:
##"fihjjjjei"
#"hjibagacbhadfaefdjaeaebgi"

def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        mg={i : magazine.count(i) for i in set(magazine)} 
        rN={i : ransomNote.count(i) for i in set(ransomNote)}
        #x=False
        if rN or rN!=mg:
            for i in rN :
                if (rN.keys(i).>=mg[i]):
                    return False
              
        return True  