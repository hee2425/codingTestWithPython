# https://school.programmers.co.kr/learn/courses/30/lessons/12945
def solution(n):
    fibonacci = [0,1]
    for i in range(2,n+1):
        fibonacci.append((fibonacci[i-2]%1234567+fibonacci[i-1]%1234567)%1234567)
    return fibonacci[-1]


##  문제에서 1234567로 나눈 나머지를 정답으로 내놓으라는 것은 문제를 꼰 것이 아니라
## int 자료형의 범위 내에 항상 값이 있을 수 있도록 한 배려이며, 
## 자료형의 크기에 제한이 있는 언어를 쓸 경우 
## (A + B) % C ≡ ( ( A % C ) + ( B % C) ) % C라는 성질을 이용해서
## 매번 계산 결과에 1234567으로 나눈 나머지를 대신 넣는 것으로 
## int 범위 내에 항상 값이 존재함을 보장할 수 있다.