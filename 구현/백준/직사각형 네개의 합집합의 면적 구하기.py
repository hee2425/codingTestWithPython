# 모든 x좌표와 y좌표는 1이상이고 100이하인 정수이다.

square = [[0 for _ in range(101)] for _ in range(101)]

for i in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    for j in range(x1, x2):
        for k in range(y1, y2):
            square[j][k] = 1
            
area = 0

for s in square:
    area += sum(s)

print(area)
