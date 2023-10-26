# import itertools
# N,M = map(int, input().split())

# nums = [i for i in range(1, N+1)]

# arr = itertools.combinations(nums, M)

# for i in arr:
#     for j in i:
#         print(j, end=' ')
    
#     print()


n, m = list(map(int, input().split()))
s = []
def dfs(start):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    
    for i in range(start, n+1):
        if i not in s:
            s.append(i)
            dfs(i+1)
            s.pop()

dfs(1)