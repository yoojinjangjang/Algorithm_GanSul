k = [[0,0,0],[1,0,0],[0,1,1]]
l = [[1,1,1],[1,1,0],[1,0,1]]

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

    for i in range(4): # 4번 회전 시켜봄

        key = rotate(key)
        print(key)
        h = [] # Lock에서 0인 부분의 인덱스를 가진 리스트
        d = [] # Key에서 1인 부분의 인덱스를 가진 리스트
        for i in range(len(lock)): # Lock에서 0인 부분의 인덱스를 찾음
            for j in range(len(lock)):
                if lock[i][j] == 0:
                    h.append([i, j])

        print(h)

        for i in range(len(key)):  # Key에서 1인 부분의 인덱스를 찾음
            for j in range(len(key)):
                if key[i][j] == 1:
                    d.append([i,j])

        print(d)

        for i in d:
            for j in range(len(i)):


            pass


    answer = True
    return answer

solution(k, l)
