'''
1이 될 때까지 : 어떠한 수 N이 1이 될 때까지 (n에서 1을 뺀다 & N을 K로 나눈다 ) 두가지를 반복적으로 선택하여 수행 ( 두번째는 나누어떨어질때만 가능 )

입력 : N k
출력 : 수행횟수 최솟값
'''

n, k = map(int, input().split())

count = 0  # 수행한 횟수

while n > 1:
    if n % k == 0:
        n //= k
        count += 1
    else:
        n -= 1
        count += 1


print(count)
