'''
Sort 실전 문제 2. 위에서 아래로

큰 수부터 작은 수의 순서로 정렬하는 프로그램을 만드시오.
'''
n = int(input())

num = []
for i in range(n):
    num.append(int(input()))

num.sort(reverse= True)
for i in num:
    print(i, end = " ")
