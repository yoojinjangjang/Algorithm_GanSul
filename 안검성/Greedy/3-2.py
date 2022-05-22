NMK = input("")
NMK = NMK.split(" ")

data = input("")
data = data.split(" ")
data.sort()

K_cnt = 0
result = 0

for i in range(int(NMK[1])):
    if K_cnt < int(NMK[2]):
        result += int(data[len(data) - 1])
        K_cnt += 1
    else:
        result += int(data[len(data) - 2])
        K_cnt = 0

print(result)
