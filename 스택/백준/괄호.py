t = int(input())
for _ in range(t):
    stack = []
    ps = input()
    isVPS = True

    for p in ps:
        if p == '(':
            stack.append('(')
        if p == ')':
            if stack:
                stack.pop()
            elif not stack:
                isVPS = False
                break
    if not stack and isVPS:
        print('YES')
    elif stack or not isVPS:
        print('NO')