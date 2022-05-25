n = int(input())
#3, 5

count = 0

if n < 5 and n != 3:
    count = -1
elif n!= 3 and n//5 == 0:
    count = n//5
else:
    for i in range((n//3)+1):
        temp = n
        temp -= (i*3)
        if temp != 0 and temp%5 == 0:
            count = temp//5 + i
            break
        elif temp == 0:
            count = i
            break
if count == 0:
    count = -1

print(count)