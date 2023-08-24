n, m = map(int, input().split())

board = []

for _ in range(n):
    board.append(input())

answer = 0
maxV = min(n,m)
for i in range(n):
    for j in range(m):
        for k in range(maxV): #정사각형 변 길이
            if ((i+k)<n) and ((j+k)<m) and (board[i][j] == board[i][j+k] == board[i+k][j] == board[i+k][j+k]):
                answer = max(answer, (k+1)**2)
print(answer)