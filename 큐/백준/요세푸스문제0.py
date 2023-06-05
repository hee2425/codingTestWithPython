from collections import deque

n, k  = map(int, input().split())
circle = deque(i for i in range(1,n+1))

answer = []
while circle:
    for i in range(1,k+1):
        if i == k:
            m = circle.popleft()
            answer.append(m)
        else:
            m = circle.popleft()
            circle.append(m)

ans = '<'+', '.join(str(_)for _ in answer) +'>'
#''.join() : 배열을 문자열로 출력
# 정수형인 경우 TypeError발생
# 리스트 정수형을 리스트 문자열로 변환한 뒤 문자열로 바꾸기
print(ans)


