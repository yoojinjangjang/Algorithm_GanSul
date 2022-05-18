n,m,k = input("n, m, k = ").split(" ")

num = input("num = ").split(" ")
num = list(map(int, num))
num.sort(reverse= True)

sum = 0
count = 0

for i in range(int(m)):
    if count < int(k):
        sum += num[0]
        count += 1

    else:
        sum += num[1]
        count = 0

print(sum)

