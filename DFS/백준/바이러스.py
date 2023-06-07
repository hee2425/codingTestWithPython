computers = int(input())
ssang = int(input())
graph = [[] for _ in range(computers+1)]
visited = [False] * (computers+1)

for _ in range(ssang):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

cnt = 0
def dfs(v):
    global cnt  # 전역 변수 선언
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(i)
            cnt +=1

dfs(1)
print(cnt)