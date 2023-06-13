from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited_dfs = [False]*(n+1)
visited_bfs = [False]*(n+1)

answer_dfs = []
answer_bfs = []

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    graph[x].sort()
    graph[y].sort()

def dfs(d):
    visited_dfs[d] = True
    answer_dfs.append(d)
    for i in graph[d]:
        if not visited_dfs[i]:
            dfs(i)


def bfs(b):
    queue = deque([b])
    visited_bfs[b] = True
    while queue:
        next = queue.popleft()
        answer_bfs.append(next)
        for i in graph[next]:
            if not visited_bfs[i]:
                queue.append(i)
                visited_bfs[i] = True
                

dfs(v)
print(*answer_dfs)
bfs(v)
print(*answer_bfs)



