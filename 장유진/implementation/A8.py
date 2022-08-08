
data = input()
result = []
value = 0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)

result.sort()
if value != 0:      # 0인 경우 제외해주기 위한 코드 추가 !
    result.append(str(value))
print(''.join(result))
