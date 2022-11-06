
import sys
input = sys.stdin.readline

N = int(input())
students = []
for _ in range(N):
    name, score = input().split()
    students.append((name,int(score)))

students.sort(key=lambda x:x[1])

for i in students:
    print(i[0],end=' ')