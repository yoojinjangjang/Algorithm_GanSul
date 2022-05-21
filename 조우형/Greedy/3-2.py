n,m,k = input("n, m, k = ").split(" ")

num = input("num = ").split(" ")
num = list(map(int, num))
num.sort(reverse= True)

sum = 0
count = 0

for i in range(int(m)):
    if count < int(k):
        sum += num[0]
        count += 1

    else:
        sum += num[1]
        count = 0

print(sum)


'''
n,m,k = map(int,input("n, m, k = ").split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1] #가장 큰 수
second = data[n-2] #두 번째로 큰 수

#가장 큰 수가 더해지는 횟수 계산
count = int(m/k+1)*k
count += m%(k+1)

result = 0
result += (count)*first #가장 큰 수 더하기
result += (m-count)*second #두 번째로 큰 수 더하기

print(result)
'''

