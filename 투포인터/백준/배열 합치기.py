# N, M = map(int, input().split())

# arr_A = list(map(int, input().split()))
# arr_B = list(map(int, input().split()))

# answer = arr_A+arr_B
# print(*sorted(answer))


###########################################
###########투 포인터 사용###################
import sys
N, M = map(int, sys.stdin.readline().split())

arr_A = list(map(int, sys.stdin.readline().split()))
arr_B = list(map(int, sys.stdin.readline().split()))

answer = []
a, b = 0,0
alen, blen = len(arr_A), len(arr_B)


while a <= alen and b<=blen:
    if a == alen:
        answer.append(arr_B[b])
        b +=1
    elif b == blen:
        answer.append(arr_A[a])
        a += 1
    else:
        if arr_A[a] < arr_B[b]:
            answer.append(arr_A[a])
            a += 1
        else:
            answer.append(arr_B[b])
            b+=1

print(*answer)
