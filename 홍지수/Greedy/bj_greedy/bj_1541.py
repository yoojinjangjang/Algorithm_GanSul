'''
잃어버린 괄호 - [boj] 1541
'''
import sys

line = sys.stdin.readline().split('-')

ans = sum(map(int, line[0].split('+')))

for i in line[1:]:
    ans -= sum(map(int, i.split('+')))

print(ans)
