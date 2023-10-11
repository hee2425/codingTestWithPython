a,b,c = map(int, input().split())

answer = 0
if a==b and b==c:
    answer = 10000 + a*1000   
elif a==b and a!=c:
    answer = 1000+a*100
elif a==c and a!=b:
    answer = 1000+a*100
elif b==c and a!=b:
    answer = 1000+b*100
elif a!=b and a!=c and b!=c:
    answer = max(a,b,c)*100


print(answer)