'''
그리디 기출 문제 3. 문자열 뒤집기
0과 1로만 이뤄진 문자열 S를 n번 뒤집어서 모두 같은 숫자로 만드는 최소 n을 구하여라

문제가 이상하다. 난 이상하지 않다.
'''

data = input('0과 1로 이루어진 문자열 입력 : ')
count0 = 0 #전부 0으로 바꾸는 경우
count1 = 0 #전부 1로 바꾸는 경우

#첫 번째 원소에 대해서 처리
if data[0] == '1':
    count0 += 1
else:
    count1 += 1

#두 번째 원소부터 모든 원소를 확인하며
for i in range(len(data)-1):
    if data[i] != data[i+1]:
        #다음 수에서 1로 바뀌는 경우
        if data[i+1] == '1':
            count0 +=1
        #다음 수에서 0으로 바뀌는 경우
        else:
            count1 += 1

print(min(count0, count1))

