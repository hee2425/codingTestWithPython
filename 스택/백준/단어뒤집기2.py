import sys

S = list(sys.stdin.readline().rstrip())
#(readline()은 \n도 받으므로, 이 공백문자를 제거하는 역할을 한다.)

print(S)
stack = ''
answer = ''
flag = False #뒤집어서 출력

for i in S:
    if flag == False:
        if i == '<':
            flag = True
            stack += i
        elif i == ' ':
            stack += i
            answer += stack
            stack = ''
        else:
            stack = i+stack
    
    else:  #정상 출력
        stack += i
        if i == '>':
            flag = False
            answer += stack
            stack = ''

print(answer + stack)


