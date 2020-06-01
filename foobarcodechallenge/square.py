# n=3
# i=[[1]*n]*n
# print(i)

matrix =[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]]
def countSquares(matrix: [[int]]) -> int:
    c=len(matrix[0])
    r=len(matrix)
    count=0
    x=0
    while x < r:
        y = x+1
        while y <= r:
            a = 0
            while a < c:
                b = a+1
                while b <= c:
                    sm = []
                    for i in matrix[x:y]:
                        sm.append(i[a:b])
                    print(sm)
                    count += 1
                    b += 1
                a += 1
            y += 1
        x += 1       
            

countSquares(matrix)    