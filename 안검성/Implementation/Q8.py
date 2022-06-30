import sys

data = sys.stdin.readline()

result = ""
result_sum = 0

for i in data:
    if i.isnumeric():
        result_sum += int(i)
    else:
        result += i

result = "".join(sorted(result))
result_sum = str(result_sum)
print(result[1:] + result_sum)
