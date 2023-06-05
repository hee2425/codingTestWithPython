import sys
from collections import deque
tc = int(input())

for i in range(tc):
    n, m = map(int, input().split())
    #n : 문서의 개수
    #m : 몇번째에 놓여있는지 나타내는 정수

    imp = deque(list(map(int, sys.stdin.readline().split())))
    cnt = 0

    while imp:
        max_v = max(imp)
        front = imp.popleft() #큐에서 하나 뽑았으니
        m -= 1 #위치가 한칸 당겨짐

        if max_v == front:  #중요도 가장 높은 수와 처음 수가 같을때
            cnt +=1
            if m <0:
                print(cnt)
                break

        else:
            imp.append(front)
            if m<0:
                m = len(imp) -1
    
