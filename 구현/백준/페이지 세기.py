
while True:
    n = int(input())
    if n == 0:
        break
    
    pages = [0 for _ in range(n+1)]
    page = input().split(',')
    for i in page:
        to_print = list(map(int, i.split('-')))
        if to_print[0] > n: #첫페이지가 페이지 범위를 넘어갈때
            continue
        if len(to_print) ==1: #범위 아닐때
            pages[to_print[0]] = 1
            continue
        if to_print[0] > to_print[1]: # 첫페이지가 나중 페이지보다 클때
            continue
        if to_print[1]> n: #나중 페이지가 페이지 범위를 넘어갈때
            to_print[1] = n
        for j in range(to_print[0], to_print[1]+1):
            pages[j] = 1

    print(sum(pages))
