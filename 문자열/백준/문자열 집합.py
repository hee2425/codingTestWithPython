n, m = map(int, input().split())

s = []
count = 0

for _ in range(n):
    s.append(str(input()))

for _ in range(m):
    word = str(input())
    if word in s:
        count+=1

print(count)