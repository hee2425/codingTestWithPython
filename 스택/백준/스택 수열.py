n = int(input())
stack = []
result = []

cur = 1
flag = True
for i in range(n):
    target = int(input())
    while cur<=target:
        stack.append(cur)
        result.append("+")
        cur += 1
    if stack[-1] == target:
        stack.pop()
        result.append("-")
    else:
        flag = False

if (flag == True):
    for i in result:
        print(i)
else:
    print("NO")