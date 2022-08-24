'''
구현 기출 문제 12. 기둥과 보 설치
가상의 2차원 벽면 N x N 크기 정사각 격자에 기둥과 보를 이용한 구조물을 설치하여 주택을 짓는다.

기둥은 바닥 위에 있거나 보의 한쪽 끝부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다.
보는 한쪽 끝부분이 기둥 위에 있거나, 또는 양쪽 끝부분이 다른 보와 동시에 연결되어 있어야 합니다.

Ex)
buld_frame = [x좌표, y좌표, 기둥 or 보, 설치 or 삭제]
기둥 = 0, 보 = 1
삭제 = 0, 설치 = 1

n = 5
bf = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
'''

n = 5
bf = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]

def possible(answer):

    for x, y, stuff in answer:
        if stuff == 0: # 기둥이면
            if [x, y-1, 0] in answer or [x-1, y, 1] in answer or [x, y, 1] in answer or y == 0:
                continue

            return False

        elif stuff == 1: #'보'면
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or [x-1, y, 1] in answer and [x+1, y, 1] in answer:
                continue
            return False

    return True


def solution(n, build_frame):
    answer = []

    for bf in build_frame:
        x, y, stuff, operation = bf

        if operation == 0: # 작업이 삭제인 경우
            if [x, y, stuff] in answer:
                answer.remove([x, y, stuff])
                if not possible(answer):
                    answer.append([x,y,stuff])
        elif operation == 1:
            answer.append([x,y,stuff])
            if not possible(answer):
                answer.remove([x,y,stuff])

    return sorted(answer)

print(solution(n, bf))