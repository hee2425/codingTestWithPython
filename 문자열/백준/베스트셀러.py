import sys
from collections import Counter
n = int(input())

books = []
for _ in range(n):
    books.append(sys.stdin.readline().rstrip())

books.sort()
count_books = Counter(books)
max_book = count_books.most_common(n=1)

print(max_book[0][0])