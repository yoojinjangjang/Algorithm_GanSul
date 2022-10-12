
# 반복 구현 n!
def factorial_iterative(n):
    result = 1
    # 1부터 n까지 수를 차례로 곱하기
    for i in range(1,n+1):
        result *= i
    return result


# 재귀 구현 n!
def factorial_recursive(n):
    if n==1 or n==0:
        return 1
    # n! = n * (n-1)!
    return n * factorial_recursive(n-1)

print(factorial_iterative(5))
print(factorial_recursive(5))