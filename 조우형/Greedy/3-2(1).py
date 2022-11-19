'''
n = 배열의 크기
m = 숫자가 더해지는 횟수
k = 같은 인덱스가 연속적으로 더해질 수 있는 횟수
'''

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

sum = 0
data.sort(reverse= True)
first = data[0]
second = data[1]

while(True):
    for i in range(k):
        if m == 0:
            break
        sum += first
        m -= 1

    if m == 0:
        break
    sum += second
    m -= 1

print(sum)


