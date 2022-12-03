def solution(N, stages):
    answer = []
    stage_num_to_fail = {}
    total_num = len(stages)
    for i in range(1,N+1):
        stage_fail_num = stages.count(i)
        if stage_fail_num == 0:
            stage_num_to_fail[i] = 0
            continue
        stage_num_to_fail[i] = stage_fail_num / total_num
        total_num -= stage_fail_num
    sorted_fail = sorted(stage_num_to_fail.items(),key = lambda item: item[0])
    sorted_fail = sorted(sorted_fail,key = lambda item: item[1],reverse=True)
    answer = [i[0] for i in sorted_fail]
    return answer


if __name__ == '__main__':
    print(solution(5,[2,MMM 1, 2, 6, 2, 4, 3, 3]))