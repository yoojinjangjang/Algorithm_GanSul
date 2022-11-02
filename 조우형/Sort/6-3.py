'''
Sort 실전 문제 3. 성적이 낮은 순서로 학생 출력하기


'''
n = int(input())
students = []
for i in range(n):
    students.append(tuple(input().split()))

def setting(data):
    return int(data[1])

students.sort(key= setting)

for i in students:
    print(i[0], end= " ")
