def all_anagrams(elements):
    if len(elements) <=1:
        return elements
    else:
        tmp = []
        for perm in all_anagrams(elements[1:]):
            for i in range(len(elements)):
                tmp.append(perm[:i] + elements[0:1] + perm[i:])

    
    return list(set(tmp))
def fun(s1,s2):
    my_dict=dict()
    my_dict2=dict()
    print(my_dict)
    x1=len(s2)
    x2=len(s1)
    # per=all_anagrams(s1)
    print(x1)
    print(x2)
    his=hash(s1)
    my_dict2[his]=s1
    print(my_dict2)
    for i in range (0,x1,1):
        y=i+x2
        hk=s2[i:y]
        print(hk)
        hi=hash(hk)
        my_dict[hi] =hk
    print(my_dict)
    # for i in per:
        # comp=hash(i)
        # print(i)
        # print(comp)
        # if comp in my_dict.keys():
            # return True
    
    # return False
    
print(fun("ab" ,"eidboaoo"))    