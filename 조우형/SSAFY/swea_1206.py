'''
swea 1206. View
n = 14
building = 0 0 3 5 2 4 9 0 6 4 0 6 0 0
'''
T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    building = list(map(int, input().split()))

    count = 0
    for i in range(2, n-2):
        ma = 0

        if building[i] > building[i-2]:
            if building[i] > building[i-1]:
                ma = max(building[i-2], building[i-1])
            else:
                continue
        else:
            continue

        if building[i] > building[i+2]:
            if building[i] > building[i+1]:
                ma = max(ma,max(building[i+1],building[i+2]))

                count += building[i] - ma
    print("#{} {}".format(test_case, count))

