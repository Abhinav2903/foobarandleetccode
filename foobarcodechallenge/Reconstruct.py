def reconstructQueue(people: [[int]]) -> [[int]]:
    result=[]
    people.sort(reverse=False,key=lambda x: (-x[0],x[1]))
    print(people)
    for i,j in people:
         result.insert(j,[i,j])
    print(result)

reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]])
