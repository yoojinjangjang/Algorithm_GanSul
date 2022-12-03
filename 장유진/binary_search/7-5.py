import sys
input = sys.stdin.readline

N = int(input())
tools = list(map(int, input().split()))
M = int(input())
customers = list(map(int, input().split()))

tools.sort()


def find_tool(tools, customer, start, end):
    if start > end:
        return False
    mid = (start + end) // 2
    if tools[mid] == customer:
        return True
    elif tools[mid] < customer:
        return find_tool(tools, customer, mid + 1, end)
    else:
        return find_tool(tools, customer, start, mid - 1)


for customer in customers:
    print('yes' if find_tool(tools, customer, 0, N-1) else 'no', end=' ')
