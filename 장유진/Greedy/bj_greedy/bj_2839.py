'''
설탕 배달 : 사탕가게에 설탕을 정확하게 N킬로 배달해야 한다. 봉지는 3킬로와  5킬로 봉지
최대한 적은 봉지를 들고가려고 한다. 봉지 몇개를 들고 가면 되는가.

입력 : N ( 배달해야하는 킬로 )
출력 : 배달하는 최소 봉지 수 ( 정확하게 만들수 없다면 -1 )
'''

import sys
input = sys.stdin.readline

n = int(input())
ans = 0
while n%5 != 0:
    if n < 3:
        print(-1)
        break
    n -= 3
    ans += 1
    print(n,'ans=',ans)

if n%5==0:
    ans += (n//5)
    print(ans)



