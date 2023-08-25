from collections import deque

a, b = map(int, input().split())

result = -1
queue = deque([(a, 1)])
while queue:
    i, cnt = queue.popleft()
    if i == b:
        result = cnt
        break

    if i*2 <=b:
        queue.append((i*2, cnt+1))
    if i*10+1<=b:
        queue.append((i*10+1, cnt+1))

print(result)