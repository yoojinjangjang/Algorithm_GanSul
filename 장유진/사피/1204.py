'''
어느 고등학교에서 실시한 1000명의 수학 성적을 토대로 통계 자료를 만들려고한다.

이때, 이 학교에서는 최빈수를 이용하여 학생들의 평균 수준을 짐작하는데, 여기서 최빈수는 특정 자료에서
가장 여러 번 나타나는 값을 의미한다.

'''

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    case_num = int(input())
    score = list(map(int,input().split()))
    score.sort()
    set_score = set(score)
    freq = []
    for i in set_score:
        freq.append(score.count(i))
    while freq.count(max(freq)) != 1:
        freq[freq.index(max(freq))] = 0
    print("#%d %d"%(case_num,freq.index(max(freq),)))


