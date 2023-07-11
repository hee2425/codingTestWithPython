f = int(input())
m = int(input())

answer = 0
if f==1: 
    answer = 8*m
elif f==5:
    answer = 8*m+4
else:
    if m%2 == 0:
        answer = 4*m+(f-1)
    else:
        answer = 4*m+(5-f)
    
print(answer)
