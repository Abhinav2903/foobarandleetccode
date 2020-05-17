def peopleIndexes(favoriteCompanies: [[str]]) -> [int]:
    a=[]
    l=len(favoriteCompanies)
    # print(l)
    for i in range (0,l):
        k=-1
        # nl=len(favoriteCompanies[i])
        # print(nl)
        
        for j in range(0,l):
            fc=set(favoriteCompanies[i])
            fcco=set(favoriteCompanies[j])
            # if(favoriteCompanies[i]==favoriteCompanies[j]):
            if(fc.issubset(fcco)):    
                k+=1
            
        if(k==0):
            a.append(i)           

    return a


print(peopleIndexes([["leetcode","google","facebook"],["leetcode","amazon"],["facebook","google"]]))
# Output: [0,1,4]     


