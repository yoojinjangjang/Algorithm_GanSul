'''
Dynamic Programming 실전 문제 3. 개미 전사

일직선으로 나열된 식량 창고에서 식량을 뺏어오려고 한다. 인접한 식략 창고를
공격하면 정찰병들이 알아챈다.
정찰병들이 알아채지 않도록 식량 창고에서 약탈할 수 있는 식량의 최대값을 구하세요.
Ex) input
4
1 3 1 5

output
8
'''
n = int(input())
foods = list(map(int, input().split()))




