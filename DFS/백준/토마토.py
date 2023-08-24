from collections import deque

#m 가로, n세로
#1익은, 0안익은, -1없음
m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

queue = deque([])
dx = [-1,1,0,0]
dy = [0,0,-1,1]
# cnt = 0 
answer = 0

# 처음 익은 토마토 좌표
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            queue.append([i,j])  

def bfs():
    while queue:
        x,y = queue.popleft() #큐에 담은 좌표
        for i in range(4):
            nx, ny = dx[i]+x, dy[i]+y
            if 0<=nx<n and 0<=ny<m and matrix[nx][ny] ==0: #안익은 토마토면
                #익음
                matrix[nx][ny] = matrix[x][y]+1 
                # cnt += 1
                queue.append([nx,ny]) #다시 큐에 익은 토마토 좌표 담기


bfs()


for a in matrix:
    for b in a:
        if b==0: #토마토가 안익은게 있으면
            print(-1)
            # break
            exit()
    answer = max(answer, max(i)) #가장 큰수구하기
print(answer-1) 
