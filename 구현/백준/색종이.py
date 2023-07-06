area =  [[0 for _ in range(101)] for _ in range(101)]

n = int(input())  #색종이 수

for i in range(n):
    x, y = map(int, input().split())

    for j in range(x, x+10):
        for k in range(y, y+10):
            area[j][k] = 1

result = 0
for a in area:
    result += sum(a)

print(result)
