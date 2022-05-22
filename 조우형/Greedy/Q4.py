'''
그리디 기출 문제 4. 만들 수 없는 금액
n개의 동전을 가지고 만들 수 없는 금액 중 최소 금액을 구하여라
'''

n = int(input("동전 개수 : "))
coin = list(map(int, input("동전 단위 : ").split()))
# coin = [3, 2, 1, 1, 9]
coin.sort()

target = 1

for x in coin:
    if target < x:
        break
    target += x

print(target)


