X = int(input())


def get_x(X):
    cnt = [0] * 30_001
    cnt[2] = 1
    cnt[3] = 1
    cnt[4] = 2
    cnt[5] = 1

    for i in range(6, X+1):
        min_temp = []
        if i%5 == 0:
            min_temp.append(1+cnt[i//5])
        elif i%3 ==0:
            min_temp.append(1+cnt[i//3])
        elif i%2 == 0:
            min_temp.append(1+cnt[i//2])
        min_temp.append(1+cnt[i-1])

        cnt[i]  = min(min_temp)
    return cnt[X]

print(get_x(X))

