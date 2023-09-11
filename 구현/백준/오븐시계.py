import sys
h,m = map(int, sys.stdin.readline().split())

c = int(input())

m += c

if m >= 60:
    h += (m//60)
    m %= 60

if h>=24:
    h -= 24

print(h, m)