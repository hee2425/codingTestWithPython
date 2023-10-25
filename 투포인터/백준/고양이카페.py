n, k = map(int, input().split())
weight = list(map(int, input().split()))
left, right = 0, n - 1

weight.sort()
answer = 0

while left < right:
    if weight[left] + weight[right] <= k:
        left += 1
        right -= 1
        answer += 1
    else:
        right -= 1
    
print(answer)
    