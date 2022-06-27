'''
구현 기출 문제 8. 문자열 재정렬
알파벳 대문자와 숫자로만 구성된 문자열이 입력으로 주어졌을 때,
모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에, 그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.
Ex) input = K1KA5CB7
Result = ABCKK13
'''
import sys
input = sys.stdin.readline()
s =""
sum = 0
for i in input:
    if i.isalpha():
        s += i
    elif i.isdigit():
        sum += int(i)
if sum != 0:
    print("".join(sorted(s))+str(sum))
else:
    print("".join(sorted(s)))
