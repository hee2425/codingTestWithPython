
def dfs(x,y):
    if graph[x][y] == '-':
        graph[x][y] = 0  #방문처리
        for ny in [1, -1]:
            Y = y+ny
            if (Y>0 and Y<m) and graph[x][Y] =="-":
                dfs(x,Y)

    if graph[x][y] == '|':
        graph[x][y] = 0  #방문처리
        for nx in [1,-1]:
            X = x+nx
            if (X>0 and X<n) and graph[X][y]=='|':
                dfs(X,y)
                
n,m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(input()))

cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == '-' or graph[i][j]=='|':
            dfs(i,j)
            cnt +=1


print(cnt)