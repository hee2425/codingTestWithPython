import sys
input = sys.stdin.readline

w, h = map(int, input().split())

def location(nswe, leng):
    if nswe == 1: #북
        return leng
    elif nswe == 2: #남
        return w+w+h-leng
    elif nswe == 3: #서
        return 2*(w+h)-leng
    elif nswe == 4: #동
        return w+leng
    
num = int(input())

stores = [0]*num
for i in range(num):
    nswe, leng = map(int, input().split())
    stores[i] = location(nswe, leng)

dk_nswe, dk_leng = map(int, input().split())
dk = location(dk_nswe, dk_leng)

all_dist = 0
answer = 0
for store in stores:
    all_dist = abs(store-dk)
    answer += min(all_dist, 2*(w+h)-all_dist)

print(answer)
