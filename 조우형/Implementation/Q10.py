k = [[1,0,1],[0,0,1],[0,0,0]]
l = [[1,1,1,1],[1,1,1,1],[1,1,1,0],[1,1,1,0]]

def rotate(key):

    temp = []
    col = len(key)
    low = len(key[0])

    for i in range(low):

        b = []
        for j in reversed(range(col)):

            b.append(key[j][i])

        temp.append(b)

    return temp

def solution(key, lock):

    check = True #자물쇠가 모두 1인 경우인지를 판별하기 위한 변수
    crash = False # 키와 자물쇠의 돌기가 충돌 났을 경우
    answer = False
    h = []  # Lock에서 0인 부분의 인덱스를 가진 리스트

    for i in lock: # 자물쇠가 모두 1인 경우 비교할 필요 없으니 바로 True를 리턴하도록 한다.
        if check == False:
            break
        for j in i:
            if j != 1:
                check = False

    if check == True:
        answer = True
        return answer

    for i in range(len(lock)):  # Lock에서 0인 부분의 인덱스를 찾음
        for j in range(len(lock)):
            if lock[i][j] == 0:
                h.append([i, j])

    for i in range(4): # 4번 회전 시켜봄
        #print(key)
        d = [] # Key에서 1인 부분의 인덱스를 가진 리스트


        #print(h)

        for i in range(len(key)):  # Key에서 1인 부분의 인덱스를 찾음
            for j in range(len(key)):
                if key[i][j] == 1:
                    d.append([i, j])

        if len(d) < len(h):  # 홈의 개수보다 돌기의 개수가 적으면 깬다
            break
        #print(d)

        for i in d:
            # 1인 인덱스들의 위치에서 0인 인덱스들 간의 차이를 구하고, 그 차이를 1인 인덱스들의 위치에 더해준 값들이
            # h 에 있는 값들인지를 확인하기 위한 부분
            x = i[0] - h[0][0]
            y = i[1] - h[0][1]

            temp = []
            true_count = 0
            for j in d: #인덱스 위치 이동 시킨 값들을 저장한 변수 temp
                temp.append([j[0]-x, j[1]-y])

            #print("움직인 좌표", temp)

            for z in temp: #temp 값 하나 하나가 원래 자물쇠의 값과 맞물리는지 확인
                crash = False
                try:
                    if z[0] < 0 or z[1] < 0:
                        continue
                    if lock[z[0]][z[1]] == 1:
                        crash = True
                        #print(z)
                        #print("충돌 발생")

                        break
                except:

                    continue

            #print("crash", crash)
            if crash == True:
                break

            for k in h:
                if k in temp:
                    true_count += 1
                else:
                    break

            if true_count == len(h):
                answer = True
                return answer

        key = rotate(key)

    return answer

print(solution(k, l))
