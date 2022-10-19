'''
괄호 변환

'''

import sys
input = sys.stdin.readline

def solution(p):

    answer = ""
    if p == "":
        return ""
    # 1. 균형 잡힌 괄호 문자열 찾기
    u = []
    cnt = 0
    i = 0
    while True:
        if p[i] == "(":
            cnt += 1
            u.append(p[i])
        elif p[i] == ")":
            u.append(p[i])
            cnt -= 1
        if cnt == 0:
            break
        i += 1
    v = p[i+1:]

    # 3. u가 올바른 괄호 문자열인지 아닌지 구분
    check = True
    stack  = []
    for i in u:
        if i == "(":
            stack.append("(")
        elif i == ")":
            if len(stack) == 0:
                check = False
                break
            stack.pop()

    if check:
        v = solution(v)
        if v is not None:
            answer = ''.join(u) + v
        else:
            answer = ''.join(u)
        return answer
    else:
        answer = '('
        v = solution(v)
        answer += v
        answer += ')'
        u = u[1:len(u)-1]
        for i in range(len(u)):
            if u[i] == "(":
                u[i] = ")"
            else:
                u[i] = "("
        answer += ''.join(u)
        return answer


if __name__ == '__main__':
    print(solution(")("))
    print()
    print(solution("()))((()"))
    print()
    print(solution("(()())()"))
    print()
    print(solution(")()()()("))