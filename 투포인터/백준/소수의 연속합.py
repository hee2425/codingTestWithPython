n = int(input())


#에라토스테네스의 체
a = [False,False] + [True]*(n-1)
primes=[]  #소수의 배열

for i in range(2, n+1):
    if a[i]:
        primes.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False

start, end = 0,0
cnt = 0

while end<=len(primes) and start<=end :
    sum_primes = primes[start:end]
    total = sum(sum_primes)

    if total == n:
        cnt+=1
        end +=1
    elif total < n:
        end += 1
    else:
        start+=1

print(cnt)