'''
Sort 기출 문제 25. 실패율

스테이지의 개수 N, 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages가 매개변수로 주어질 때,
실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨 있는 배열을 return 하세요.

Ex)
intput case 1.
N = 5
stages = 2 1 2 6 2 4 3 3
result = [3,4,2,1,5]

N = 4
stages = 4 4 4 4 4
result = [4,1,2,3]
'''
n = int(input())
stages = list(map(int, input().split()))
def solution(N, stages):
    stages.sort()
    result = {}

    for i in range(1, N+1):
        result[i] = stages.count(i) / len(stages)`

        for j in range(len(stages)):
            if stages[j] != i:
                stages = stages[j:]
                break

    result = sorted(result.items(), key = lambda x : (x[1]), reverse= True)
    answer = [x[0] for x in result]
    return answer