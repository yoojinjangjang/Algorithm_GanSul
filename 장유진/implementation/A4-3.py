
input_data = input()
row = int(input_data[1])
column = ord(input_data[0]) - ord('a') +1

# 나이트가 이동할 수 있는 8가지 방향
steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    if 1 <= next_row <= 8 and 1 <= next_column <= 8:
        result += 1

print(result)