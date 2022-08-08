'''Q8: 문자열 재정렬
알파벳 대문자와 숫자(0~9)로 이루어진 문자열 입력
모든 알파벳 오름차순으로 정렬 뒤, 모든 숫자 더한 값 이어서 출력
입력: 문자열 S
출력: 요구하는 정답
'''
import sys
input = sys.stdin.readline

s = list(input())
s.remove('\n')
num_sum = 0
ans = []
for i in s:
    if i in "0123456789":
        num_sum += int(i)
    else:
        ans.append(i)

ans.sort()
print(''.join(ans),end='')
print(num_sum)

