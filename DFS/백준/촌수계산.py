n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)

answer = []

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(v, chonsu):
    chonsu +=1
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(i, chonsu)

    if v == b:
        answer.append(chonsu)

dfs(a,0)
if len(answer) == 0:
    print(-1)
else:
    print(answer[0]-1)
