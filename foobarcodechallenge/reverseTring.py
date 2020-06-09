def reverseString(s: [str]) -> None:
    l=len(s)
    left=0
    right=l-1
    while(left<right):
        s[left],s[right]=s[right],s[left]
        left+=1
        right-=1
    print(s)
    # one linear just do s.reverse()

    # another with for loop 
        # for e in range(l//2):
            # l=l-1
            # tmp=s[l]
            # s[l]=s[e]
            # s[e]=tmp

reverseString(["h","e","l","l","o"])    
# ["A"," ","m","a","n",","," ","a"," ","p","l","a","n",","," ","a"," ","c","a","n","a","l",":"," ","P","a","n","a","m","a"]
# ["a","m","a","n","a","P"," ",":","l","a","n","a","c"," ","a"," ",",","n","a","l","p"," ","a"," ",",","n","a","m"," ","A"]