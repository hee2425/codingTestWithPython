n = int(input())

gradeClass = [[] for _ in range(n)] 

same = [0]*n 

for i in range(len(gradeClass)):
    gradeClass[i] = list(map(int, input().split()))
    same[i] = [0]*n  #2차 배열

for i in range(5): #학년별
    for j in range(n): #학생별
        for k in range(j+1, n): #다음 학생과 비교
            if gradeClass[j][i] == gradeClass[k][i]:
                same[k][j] = 1
                same[j][k] = 1

count = []
for s in same:
    count.append(sum(s))


print(count.index(max(count))+1)
