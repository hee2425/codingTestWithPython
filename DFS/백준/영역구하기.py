import sys
sys.setrecursionlimit(10000)

m, n, k = map(int, sys.stdin.readline().split())

graph  = [[False for _ in range(m)]for _ in range(n)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            graph[x][y] = True

def dfs(x,y,count):
    graph[x][y] = True
    for dx, dy in d:
        x, y = x+dx, y+dy
        if(0<=x<n) and (0 <= y<m) and graph[x][y] == 0:
            count = dfs(x,y, count+1)

    return count

area = []
d = [(1,0),(-1,0),(0,1),(0,-1)]

for y in range(m):
    for x in range(n):
        if graph[x][y]  == False:
            area.append(dfs(x, y, count=1))

print(len(area))
print(*sorted(area))
