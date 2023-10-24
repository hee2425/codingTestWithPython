n, m = map(int, input().split())
numbers = list(map(int, input().split()))

answer = 0
start, end = 0,0

while end <=n and start<=end:
    sumnum = numbers[start:end]
    total = sum(sumnum)

    if total == m:
        answer+=1
        end += 1
    elif total<m:
        end+=1
    else:
        start+=1

print(answer)

    
