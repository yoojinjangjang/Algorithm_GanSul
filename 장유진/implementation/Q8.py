'''
문자열 재정렬 : 알파벳 대문자와 숫자(0~9)로만 구성된 문자열 입력
: 모든 알파벳을 오름차순으로 정렬하여 이어수 출력 뒤 모든 숫자를 더한 값을 이어서 출력

입력 : 문자열 S
출력 : 요구하는 정답
'''

import sys
input = sys.stdin.readline
num = 0
al = []
s = input()
for i in s:
    if i in '0123456789':
        num += int(i)
    else:
        al.append(i)

for i in sorted(al)[1:]:
    print(i,end='')
print(num)
