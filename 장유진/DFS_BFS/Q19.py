'''
연산자 끼워넣기
'''
import sys
from itertools import permutations
input = sys.stdin.readline


n = int(input())
a = list(map(int,input().split()))
op_num = list(map(int,input().split()))
ops = ['+','-','*','//']
op_input = []
for i in range(4):
    op_input += [ops[i]] * op_num[i]


def cal(a,b,op):
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    elif op == '*':
        return a*b
    else:
        if a < 0:
            return -(-a//b)
        else:
            return a//b

def cal_op(a,per):
    x = cal(a[0], a[1], per[0])
    for i in range(1,len(per)):
        x = cal(x,a[i+1],per[i])
    return x

answers = []
for per in set(permutations(op_input,n-1)):
    print(per)
    answers.append(cal_op(a,per))
print(max(answers))
print(min(answers))


