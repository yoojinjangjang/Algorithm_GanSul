'''
럭키 스트레이트 : 점수가 특정 조건 만족 시에만 사용 가능
: 현재 캐릭터 점수 N , 자릿수를 기준 점수 N을 반으로 나누어 왼쪽 부분의 각 자릿수의 합과 오른쪽 부분의 각 자릿수의 합을 더한 값이 동일

입력 : 점수 N , N의 자릿수는 항상 짝수
출력 : 사용가능시 'LUCKY', 불가능시 'READY'
'''
n = input()
l = int(len(n)/2)
s = 0
b = 0
for i in n[:l]:
    s += int(i)
for j in n[l:]:
    b += int(j)
if s==b:
    print('LUCKY')
else:
    print('READY')

