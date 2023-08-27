word = input()

croatia = ['c=','c-','dz=','d-','lj','nj','s=','z=']

cnt = 0

for c in croatia:
    word = word.replace(c,"@")

print(len(word))
