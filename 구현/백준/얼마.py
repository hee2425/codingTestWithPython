tc = int(input())

for _ in range(tc):
    total = 0
    s = int(input())
    n = int(input())

    total += s
    for i in range(n):
        q, p = map(int, input().split())
        total += (q*p)

    print(total)
