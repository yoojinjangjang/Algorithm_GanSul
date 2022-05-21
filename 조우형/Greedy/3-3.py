row,col = map(int, input("?x? = ").split())

result = 0
for i in range(row):
    data = list(map(int, input("num = ").split()))
    min_num = min(data)

    result = max(result,min_num)

print(result)
