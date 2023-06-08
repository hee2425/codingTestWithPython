import sys
sys.setrecursionlimit(10**4)
tc = int(input())

def dfs(v):
    global answer
    visited[v] = True  #방문
    next = graph[v]
    if not visited[next]: #다음 방문 체크
        dfs(next) #방문 안했으면 재귀
    else : #다음 방문했으면 사이클이다
        answer +=1

for _ in range(tc):
    n = int(input())
    graph = [0] + list(map(int, input().split()))
    visited = [False]*(n+1)
    answer = 0
    for i in range(1, n+1):
        if not visited[i]: #방문 안했으면
            dfs(i) #재귀
    print(answer)

