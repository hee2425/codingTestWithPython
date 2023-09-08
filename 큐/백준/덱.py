from collections import deque
import sys

n = int(input())
deque = deque()

for _ in range(n):
    command = sys.stdin.readline().split()
    
    if 'push' in command[0]:
        if command[0] == 'push_front':
            deque.appendleft(command[1])
        else:
            deque.append(command[1])
    elif 'pop' in command[0]:
        if command[0] == 'pop_front':
            if len(deque)>0:
                print(deque[0])
                deque.popleft()
            else:
                print(-1)
        else:
            if len(deque)>0:
                print(deque[-1])
                deque.pop()
            else:
                print(-1)
    elif command[0] == 'size':
        print(len(deque))
    elif command[0] == 'empty':
        if len(deque)>0:
            print(0)
        else:
            print(1)
    elif command[0] == 'front':
        if len(deque)>0:
            print(deque[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if len(deque)>0:
            print(deque[-1])
        else:
            print(-1)


