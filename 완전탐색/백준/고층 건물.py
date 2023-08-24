n = int(input())
building = list(map(int,input().split()))

#기울기
def slope(x1, y1, x2, y2):
    return (y2-y1)/(x2-x1)

answer = 0

for i1, h1 in enumerate(building):  #리스트 원소에 순서값 부여
    cnt_right, cnt_left = 0,0
    x1 = i1+1
    y1 = h1

    #오른쪽
    com_slope_right = None #비교 기울기
    
    for i2 in range(i1+1, n):
        x2 = i2+1
        y2 = building[i2]

        cur_slope = slope(x1, y1, x2, y2) #현재 기울기

        if com_slope_right is None or (com_slope_right < cur_slope):
            #비교할 기울기가 없거나, 비교기울기보다 현재 기울기가 클경우
            cnt_right += 1
            com_slope_right = cur_slope

    #왼쪽
    com_slope_left = None

    for i3 in range(i1-1,-1,-1):
        x3 = i3+1
        y3 = building[i3]

        cur_slope = slope(x1, y1, x3, y3)

        if com_slope_left is None or (com_slope_left > cur_slope):
            #비교할 기울기가 없거나, 비교 기울기보다 현재 기울기가 작을 경우
            cnt_left +=1
            com_slope_left = cur_slope

    answer = max(answer, (cnt_right+cnt_left))
print(answer)

