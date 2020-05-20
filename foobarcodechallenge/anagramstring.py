def all_anagrams(elements):
    if len(elements) <=1:
        return elements
    else:
        tmp = []
        for perm in all_anagrams(elements[1:]):
            for i in range(len(elements)):
                tmp.append(perm[:i] + elements[0:1] + perm[i:])

    # print(len(set(tmp)))
    return list(set(tmp))  


def find_anagrams(s,perm):
    ana_index=[]
    if (s=="") :
        return [] 
    
    x=all_anagrams(perm)
    
    for i in range (0,len(s)+1):
        ns=s[i:i+len(perm)]
        if ns in x and ns!='':
            ana_index.append(i) 
    return ana_index

print(find_anagrams("acdcaeccde","c"))        
#"acdcaeccde"
#"c"