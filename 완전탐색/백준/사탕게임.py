#오른쪽, 아래 비교

n = int(input())

board = [list(input()) for _ in range(n)]

def count(board):
    maxCnt = 0
    for i in range(n):
        cnt = 1
        for j in range(1,n):
            if board[i][j] == board[i][j-1]:
                cnt +=1
            else:
                cnt =1
            maxCnt = max(cnt, maxCnt)
    return maxCnt

answer = 0
for i in range(n):
    for j in range(n):
        if j+1<n: #오른쪽 비교
            #바꾸기
            board[i][j], board[i][j+1] == board[i][j+1], board[i][j]
            
            cnt = count(board)
            answer = max(cnt, answer)
            board[i][j], board[i][j+1] == board[i][j+1], board[i][j]

        if i+1<n: #아래 비교
            #바꾸기
            board[i][j], board[i+1][j] == board[i+1][j], board[i][j]

            cnt = count(board)
            answer = max(cnt, answer)
            board[i][j], board[i+1][j] == board[i+1][j], board[i][j]

print(answer)