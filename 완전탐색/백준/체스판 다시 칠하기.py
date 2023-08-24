n, m = map(int, input().split())
board = []
answer = []

for _ in range(n):
    board.append(input())

for a in range(n-7):
    for b in range(m-7):
        black = 0  #검은색 카운트
        white = 0  #흰색 카운트

        for i in range(a, a+8):
            for j in range(b,b+8):
                if(i+j)%2 == 0: #짝수
                   if board[i][j]=="B":
                        white +=1
                   else:
                       black +=1
                else: #홀수
                    if board[i][j] =="B":
                        black += 1
                    else:
                        white += 1

        answer.append(white)
        answer.append(black)

print(min(answer))

