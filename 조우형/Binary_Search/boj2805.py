'''
Binary Search 백준 10026. 나무 자르기

상근이가 필요한 만큼 M미터의 나무를 가져가기 위해 톱날로 자를 높이를 H미터로 지정하였을 때,
적어도 M미터를 가져가기 위한 톱날의 높이의 최댓값을 구하세요.
'''
n, m = map(int, input().split())
trees = list(map(int, input().split()))

trees.sort()
start = 0
end = max(trees)

resul = 0
while(start<= end):
    total = 0
    mid = (start+end)//2
    for x in trees:
        if x > mid:
            total += x - mid

    if total < m:
        end = mid -1
    else:
        result = mid
        start = mid + 1

print(result)


