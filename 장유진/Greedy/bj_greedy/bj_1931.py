'''
회의실 배정 : 한개의 회의실을 사용하고자 하는 N개의 회의에 대한 회의실 사용표
            각 회의 I에 대한 시작시간,끝 시간 --> 겹치지 않게 사용할 수 있는 회의의 최대 갯수

입력 : N ( 회의 수 )
     각 회의 정보 ( 시작시간,끝시간)
출력 : 최대 사용 회의 최대 개수
'''
import sys
input = sys.stdin.readline

n = int(input())
data = []
for i in range(n):
    data.append(tuple(map(int,input().split())))
data.sort(key=lambda x:x[0])
data.sort(key=lambda x:x[1])    # 종료시간으로 정렬
end = data[0][1]
count = 1
for i in range(1,n):
    if data[i][0] >= end:
        count += 1
        end = data[i][1]
print(count)