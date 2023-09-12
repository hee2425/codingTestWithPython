def dfs(x,y,number):
    
    if len(number) == 6:
        if number not in sixNumbers:
            sixNumbers.append(number)
        return
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    for k in range(4):
        nx = x+dx[k]
        ny = y+dy[k]

        if (0<=nx<5) and (0<=ny<5):
            dfs(nx,ny, number+graph[nx][ny])

    
graph = []
for _ in range(5):
    graph.append(list(input().split()))

sixNumbers = []

for i in range(5):
    for j in range(5):
        dfs(i,j, graph[i][j])

print(len(sixNumbers))