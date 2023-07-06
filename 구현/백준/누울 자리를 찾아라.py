# 2칸이상의 빈칸이면 누울 수 있음
# 무조건 벽이나 짐에 닿음
# 즉, 가로일 경우 행을 기준으로 2칸 이상 있으면 1개로 침
# 세로일 경우는 열을 기준으로 2칸 이상이면 1개로 침
n = int(input())

garo_sero = [0,0]

room = []
for _ in range(n):
    room.append(list(map(str, input())))


for x in range(n):
    garo, sero = 0, 0
    for y in range(n):
        if room[x][y] == '.':
            garo +=1

        # X만났을때까지 
        elif room[x][y] == 'X':
            if garo >= 2:
                garo_sero[0] += 1
            garo = 0

        if room[y][x] == ".":
            sero += 1
            
        # X만났을때까지 
        elif room[y][x] == 'X':
            if sero >= 2:
                garo_sero[1] += 1
            sero = 0

        #끝까지 갔을때
        if y == n-1:
            if garo>=2:
                garo_sero[0] +=1
            if sero>=2:
                garo_sero[1] += 1

    
print(*garo_sero)
