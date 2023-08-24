a, p = map(int, input().split())
dlist = [a]

def square_p(x):
    x = int(x) ** p
    return x

while True:
    num = sum(map(square_p, str(dlist[-1])))
    if num in dlist:
        break
    dlist.append(num)

print(dlist.index(num))  #같은 숫자의 인덱스