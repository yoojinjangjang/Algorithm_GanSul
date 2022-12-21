'''
그래프 이론. 서로소 집합 알고리즘


```1``` union(합집합) 연산을 확인하여, 서로 연결된 두 노드 A, B를 확인한다.

 		1. A와 B의 루트 노드 A', B'를 각각 찾는다.
        2. A'를 B'의 부모 노드로 설정한다(B'가 A'를 가리키도록 한다.)

```2``` 모든 union(합집합) 연산을 처리할 때까지 ```1```번 과정을 반복한다.
'''


def find_parents(number):

    if parents[number] != number:
        return find_parents(parents[number])

    return number


def union(a, b):
    a = find_parents(a)
    b = find_parents(b)

    if a < b:
        parents[b] = a
    else:
        parents[a] = b


n, k = map(int, input().split())
numbers = [i for i in range(n + 1)]
unions = []
for i in range(k):
    one, two = map(int, input().split())
    unions.append([one, two])

parents = [i for i in range(n + 1)]

for i in unions:
    one = i[0]
    two = i[1]

    union(one, two)

print("각 원소가 속한 집합 : ", end="")
for i in range(1, n+1):
    print(find_parents(i), end=" ")

print()

print("부모 테이블 : ", end="")
for i in range(1, n+1):
    print(parents[i], end=" ")


