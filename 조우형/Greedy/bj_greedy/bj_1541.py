'''
백준 그리디 1541
입력 받은 식에 적절하게 괄호를 쳐서 이 식의 값을 최소로 만들자

Ex) 입력 : 55-50+40
출력 : 35
'''
import sys
inp = sys.stdin.readline().split('-')
res = sum(list(map(int, inp[0].split('+'))))
for i in inp[1:]:
    res -= sum(list(map(int, i.split('+'))))

print(res)