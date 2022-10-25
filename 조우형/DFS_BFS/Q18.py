'''
DFS/BFS 기출 문제 18. 괄호 변환
'(' 와 ')' 로만 이루어진 문자열이 있을 경우, '('의 ')'의 개수가 같다면 이를 균형잡힌 괄호 문자열이라고 한다.
'(' 와 ')' 의 짝도 모두 맞을 경우에는 이를 올바른 괄호 문자열이라고 부른다.
균형 잡힌 문자열이지만 올바른 문자열이 아닌 경우 변환을 통해 올바른 괄호 문자열로 만들 수 있다.

Ex)
input : ()))((()
output : ()(())()
'''

w = input()
def divide(w):
    #
    left = 0
    right = 0
    for i in range(len(w)):
        if w[i] == "(":
            left += 1
        else:
            right += 1

        if left == right:
            return i

def check_pair(u):

    left = 0
    right = 0
    for i in u:
        if i == '(':
            left += 1

        elif left >= 1 and i == ')':
            right += 1

        else:
            return False

    return True

def solution(p):
    answer = ''

    if not p:
        return answer

    idx = divide(p) + 1
    u = p[:idx]
    v = p[idx:]

    if check_pair(u):
        answer = u + solution(v)
    else:
        answer = "("
        answer += solution(v)
        answer += ")"

        u = u[1:-1]

        for i in u:
            if i == "(":
                answer += ")"
            else:
                answer += "("

    return answer

print("solution = " , solution(w))