n = int(input())

line = 0
cnt = 0 # 1,3,6...

while n>cnt:
    line +=1
    cnt += line

order = line-(cnt-n)  #라인의 몇번째인지
if line %2 ==0:
    son = order
    mother = line-son+1

else: 
    mother = order
    son = line-mother+1

print(f'{son}/{mother}')