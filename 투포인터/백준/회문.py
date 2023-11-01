#회문 : 0, 유사회문:1, 그외:2
import sys

def check(word, left, right):
    while left<right:
        if word[left] == word[right]:
            left+=1
            right-=1
        else:
            leftdel = deleteCheck(word, left+1, right)
            rightdel = deleteCheck(word, left, right-1)

            # 유사회문
            if leftdel or rightdel:
                return 1
            # 회문,유사회문 아닐때
            else:
                return 2
    # 회문
    return 0
            
def deleteCheck(word, left, right):
    while left<right:
        if word[left] == word[right]:
            left+=1
            right-=1
        else:
            # 유사회문도 아님
            return False
    # 유사회문
    return True



n = int(input())
for _ in range(n):
    word = sys.stdin.readline().rstrip()

    left = 0
    right = len(word)-1

    print(check(word, left, right))
            

