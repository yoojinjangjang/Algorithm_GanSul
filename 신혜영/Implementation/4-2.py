import sys

N = int(input())

hour = 0
min = 0
sec = 0

cnt = 0

if N > 24:
    exit(0)

while True:
    if sec == 59:
        min += 1
        sec = 00
    else:
        sec += 1

    if min == 60:
        hour += 1
        min = 0

    if '3' in str(hour) or '3' in str(min) or '3' in str(sec):
        cnt += 1

    if hour == N+1 and min == 00 and sec == 00:
        break
        
print(cnt)
