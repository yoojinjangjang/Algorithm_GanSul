'''
문자열 압축 : 1개 이상의 길이 단위로 압축을 해서 가장 짧은 것의 길이를 반환

입력 : 문자열 S
출력: 가장 짧은 문자열의 길이
'''


def solution(s):
    answer = 100000
    len_s = len(s)
    for i in range(1, len_s + 1):

        tmp = s[0:i]
        count = len(tmp)
        j = i
        dup_count = 1
        while j + i <= len_s:
            aft = s[j:j + i]
            if tmp != aft:
                if dup_count != 0:
                    count += len(str(dup_count))
                    dup_count = 0
                count += i
            else:
                dup_count += 1
            tmp = aft
            j += i
        if dup_count != 0:
            count += len(str(dup_count))

        count += len(s[j:])
        print("count: ", count, "i = ", i)

        answer = min(answer, count)

    return answer
