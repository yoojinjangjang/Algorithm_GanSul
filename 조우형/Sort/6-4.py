'''
Sort 실전 문제 4. 두 배열의 원소 교체

N의 크기인 두 배열 A와 B의 원소를 서로 최대 K번 교체하여
A의 원소의 합이 최대가 되도록 만들어라.

Ex)
input
5 3
1 2 5 4 3
5 5 6 6 5

output
26
'''
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = sum(a)
for i in range(k):
    a.sort()
    b.sort()

    a[0], b[-1] = b[-1], a[0]
    if max(ans, sum(a)) == ans:
        a[0], b[-1] = b[-1], a[0]
        break
    ans = max(ans, sum(a))

print(ans)


