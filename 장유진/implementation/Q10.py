'''Q10: 자물쇠와 열쇠
https://school.programmers.co.kr/learn/courses/30/lessons/60059
자물쇠의 모든 홈을 채워 비어있는 곳이 없어야 열 수 있다.


'''
import copy

def solution(key, lock):
    key_len = len(key)
    lock_len = len(lock)
    board_len = 2 * (key_len - 1) + lock_len
    board = [[0] * board_len for _ in range(board_len)]
    # 새로운 보드를 만드는 코드
    for i in range(key_len - 1, board_len - key_len + 1):
        for j in range(key_len - 1, board_len - key_len + 1):
            board[i][j] = lock[i - key_len + 1][j - key_len + 1]

    # 90도씩 회전하며 검사
    for k in range(4):
        key = rotate(key, key_len)

        for i in range(0, board_len - key_len + 1):
            for j in range(0, board_len - key_len + 1):
                tmp = match(i, j, board, key, key_len)

                if unlock(tmp,board_len,key_len,lock_len):
                    return True

    return False


def rotate(key, key_len):  # 회전 메소드

    tmp = [[0] * key_len for _ in range(key_len)]
    for i in range(0, key_len):
        for j in range(0, key_len):
            tmp[j][key_len - 1 - i] = key[i][j]
    return tmp


def match(x, y, board, key, key_len):  # 새로 만든 보드판에 자물쇠와 열쇠를 매치시키는 메소드
    tmp = copy.deepcopy(board)
    for i in range(x, x + key_len):
        for j in range(y, y + key_len):
            tmp[i][j] += key[i - x][j - y]
    return tmp


def unlock(board, board_len, key_len, lock_len):  # 자물쇠와 열쇠가 매칭 된 곳의 unlock 여부 판단
    cnt = 0
    for i in range(key_len - 1, board_len - key_len + 1):
        for j in range(key_len -1, board_len - key_len + 1):
            if board[i][j] == 1:
                cnt += 1

    return True if cnt == (lock_len * lock_len) else False



if __name__ == '__main__':
    key = [[0,0,0],[1,0,0],[0,1,1]]
    lock = [[1,1,1],[1,1,0],[1,0,1]]
    print(solution(key,lock))