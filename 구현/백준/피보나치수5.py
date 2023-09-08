n = int(input())

pibonachi = [0,1]

for i in range(n-1):
    pibonachi.append(pibonachi[i]+pibonachi[i+1])

print(pibonachi[n])