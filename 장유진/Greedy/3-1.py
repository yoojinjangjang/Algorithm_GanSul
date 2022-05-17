'''
거스름돈 :500원,100원,50원,10원 무한히 존재한다. 거슬러줘야 할 돈 N원일때 거슬러 줘야 할 동전의 최소 개수를 구하라. ( N은 항상 10의 배수 )

입력 : N
출력 : 거슬러 줄 동전의 수
'''

n = int(input())
count = 0  # 동전의 수
coin = [500, 100, 50, 10]
i = 0
while True:
    count += n // coin[i]
    n %= coin[i]
    if n == 0:
        break
    else:
        i += 1

print(count)

