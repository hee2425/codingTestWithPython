
s = list(input().rstrip())
t = list(input().rstrip())

def step1(t):
    t.pop()
    return t

def step2(t):
    t.pop()
    t.reverse()
    return t

answer = False
while t:
    if t[-1] == 'A':
        step1(t)
    elif t[-1] == 'B':
        step2(t)

    if s == t:
        answer = True
        break

    
if answer:
    print(1)
else:
    print(0)