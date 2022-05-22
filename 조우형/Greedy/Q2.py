'''
그리디 기출문제 2. 곱하기 혹은 더하기
숫자 문자열 S가 주어졌을때, 왼쪽부터 오른쪽으로 한자리씩 모든 숫자의
더하기 혹은 곱셈을 하여 만들어질 수 있는 가장 큰 수를 출력하시오.

s : 입력 숫자 문자열
result : 최대값
'''

s = input("숫자 입력 : ")
result = 0
for i in s:
    i = int(i)
    if result <= 1 or i <= 1:
        result += i
    else:
        result *= i

print(result)
