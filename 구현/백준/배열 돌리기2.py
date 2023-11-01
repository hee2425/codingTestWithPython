import sys

n,m,r = map(int, sys.stdin.readline().split())\

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

def turn(i, j , n, m):
    top = arr[i][j]
    bottom = arr[n-1][m-1]
    left = arr[n-1][j]
    right = arr[i][m-1]

    #top
    for y in range(j, m-1): 
        arr[i][y] = arr[i][y+1]
    #bottom
    for y in range(m-1, j, -1): 
        arr[n-1][y] = arr[n-1][y-1]
    #left
    for x in range(n-1,i,-1): 
        arr[x][j] = arr[x-1][j]
    #right
    for x in range(i, n-1):
        arr[x][m-1] = arr[x+1][m-1]

    arr[i+1][j] = top
    arr[n-2][m-1] = bottom
    arr[n-1][j+1] = left
    arr[i][m-2] = right

cycle = (n-1)*2+(m-1)*2
for i in range(min(n,m) // 2):
    for _ in range(r%cycle):
        turn(i, i, n-i, m-i)
    cycle -=8  #둘레 차이 8칸씩 차이

for j in arr:
    print(*j)



