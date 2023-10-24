import sys
N, S = map(int, input().split())

numbers = list(map(int, sys.stdin.readline().split()))

start, end = 0, 0
answer = sys.maxsize
sum = 0

while True:
    if sum>=S:
        answer = min(answer, end-start)
        sum -= numbers[start]
        start += 1
    elif end == N:
        break
    else:
        sum += numbers[end]
        end += 1

if answer == sys.maxsize:
    print(0)
else:
    print(answer)