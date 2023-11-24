from collections import deque

n, k = map(int, input().split())

dq = deque(str(i) for i in range(1,n+1))

answer = []
while dq:
    for i in range(k):
        if i == k-1:
            s = dq.popleft()
            answer.append(s)
        else:
            dq.rotate(-1)
            
print("<", end='')
print(', '.join(answer), end='')
print(">", end='')
    
