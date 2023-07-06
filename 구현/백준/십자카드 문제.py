# 시계수 구하는 함수
def clocksu(num):  
    clocknum = num
    for _ in range(3):
        num = (num%1000)*10 + num//1000  #앞자리 숫자 뒤로 이동
        if clocknum > num:
            clocknum = num  #시계수
    return clocknum


clocknum = clocksu(int(''.join(input().split())))  #입력받은 수의 시계수

i = 1111 
answer = 0
while(i<=clocknum):   #1111부터 개수 세기
    if clocksu(i) == i: # 1111부터 수의 시계수와 비교
												# i에 0이 포함되어있을경우 어차피 시계수와 다르므로 카운트 안셈
        answer += 1 
    i += 1
print(answer)
