'''
구현 기출 문제 9. 문자열 압축
문자열에서 같은 값이 연속해서 나타나는 것을 그 문자의 개수와 반복되는 값으로
표현하여 더 짧은 문자열로 줄여서 표현해보세요.
압축할 문자열 s가 주어질 때, 위에 설명한 방법으로 압축한 문자열 중 가장 짧은
것의 길이를 구하세요.

Ex) input = aabbaccc
result = 7

2a2ba3c
'''
import sys
s = "abcabcabcabcdededededede"

def solution(s):

    m = len(s)
    for i in range(1, len(s) // 2 + 1):

        start = s[:i]
        cnt = 1
        temp = ""

        for j in range(i, len(s), i):

            if start == s[j:j + i]:
                cnt += 1
            else:
                if cnt != 1:
                    temp += str(cnt) + start
                else:
                    temp += start
                start = s[j:j + i]
                cnt = 1

        if cnt != 1:
            temp += str(cnt) + start
        else:
            temp += start

        print("temp= ", len(temp))
        print("m = ",m)
        m = min(m, len(temp))

    answer = m
    return answer

print(solution(s))