def maxVowels(s: str, k: int) -> int:
    vowels="aeiou"
    maxvp=ans=0
    for i,c in enumerate(s):
        # print(i)
        # print(c)
        if(c in vowels):
            maxvp+=1
        if(i >= k and s[i - k] in vowels):
            maxvp-=1
        ans=max(ans,maxvp)
    return ans

print(maxVowels("aeiou",2))   