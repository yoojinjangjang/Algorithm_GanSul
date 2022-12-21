'''
그래프 이론. 개선된 서로소 집합 알고리즘 소스코드

union 연산 이후에 find 연산을 수행하면 해당 노드의 루트 노드가
바로 부모 노드가 된다. 경로 압축 기법을 이용하게 되면 루트 노드에
더욱 빠르게 접근할 수 있다.
'''


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int,input().split())
parent = [i for i in range(v+1)]

for i in range(e):
    one, two = map(int, input().split())
    union_parent(parent, one, two)

print("각 원소가 속한 집합 : ", end="")
for i in range(1, v+1):
    print(find_parent(parent, i), end=" ")

print()

print("부모 테이블: ", end="")
for i in range(1, v+1):
    print(parent[i], end=" ")



