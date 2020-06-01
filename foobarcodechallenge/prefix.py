def isPrefixOfWord(sentence, searchWord) -> int:
    l=len(searchWord)
    sen=sentence.split()
    # sw=searchWord.split() 
    cnt=1
    for i in sen:
        if(l<=len(i)):
            x=i[:l]
            print(x is searchWord)
            if(x==searchWord):
                return cnt  
        cnt+=1
    return -1

print(isPrefixOfWord("this problem is an easy problem","pro"))    