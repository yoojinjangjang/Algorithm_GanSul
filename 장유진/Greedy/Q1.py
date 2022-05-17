'''
모험가 길드 : 공포도가 x인 모험가는 반드시 x명 이상으로 구성한 모험가 그룹에 참여
- 몇 명의 모험가는 마을에 남아 있어도 된다.

입력 : N ( 모험가 수 )
     모험가의 공포도 값

출력 : 그룹수의 최댓값
'''


n = int(input())
data = list(map(int, input().split()))
count = 0
data.sort(reverse=True)
while True:
    n -= data[-n]
    if n<0:
        break
    count +=1
print(count)



'''
        
n = int(input())
data = list(map(int,input().split()))
count = 0
data.sort()
ans = 0
for i in data:
    count +=1
    if count >= i:
        ans +=1
        count = 0

print(ans)

'''