import sys
from collections import deque  #deque 임포트 하는 것이 더 빠름

queue = deque()
n = int(sys.stdin.readline())

for _ in range(n):
    q = sys.stdin.readline().split()

    if q[0] == 'push':
        queue.append(q[1])
    elif q[0] == 'pop':
        if not queue:
            print(-1)
        else:
            print(queue.popleft())
    elif q[0] == 'size':
        print(len(queue))
    elif q[0] == 'empty':
        if not queue:
            print(1)
        else:
            print(0)
    elif q[0] == 'front':
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif q[0] == 'back':
        if not queue:
            print(-1)
        else:
            print(queue[-1])