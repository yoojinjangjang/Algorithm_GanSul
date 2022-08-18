'''
Q12. 기둥과 보
https://velog.io/@yoojinjangjang/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-60061
'''

def check(answer):
    for x,y,a in answer:
        if a == 0: #기둥인 경우
            if y==0 or [x,y-1,0] in answer or [x-1,y,1] in answer or [x,y,1] in answer:
                continue
            return False
        elif a == 1: #보인 경우
            if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer):
                continue
            return False
    return True



def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x,y,a,b = frame
        if b==0: #삭제인 경우
            answer.remove([x,y,a])
            if not check(answer):
                answer.append([x,y,a])
        elif b==1: #설치인 경우
            answer.append([x,y,a])
            if not check(answer):
                answer.remove([x,y,a])
    return sorted(answer)

if __name__ == '__main__':
    print(solution(5,[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))