'''
구현 기출 문제 14. 외벽 점검
공사 중인 외벽에 취약 지점들을 점검한다.
'''

from itertools import permutations

n = 12
weak = [1,3,4,9,10]
dist = [3,5,7]



def solution(n, weak, dist):

    #원형 외벽을 일자로 나열하여 처리한다. 무수히 반복되는 경우였으면 나머지 연산(%12)을 이용하였을 것 같은데, 원형이지만 한번만 지나가면 되기 때문에 일자로 나열해서 간편하게 해결해보도록 한다.
    for i in range(len(weak)):
        weak.append(weak[i] + n)

    print(weak)



    answer = 0
    return answer


solution(n, weak, dist)