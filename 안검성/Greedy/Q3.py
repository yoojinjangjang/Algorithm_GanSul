S = input()

oneCnt = 0
flip = False

for i in range(len(S)):
    if flip == False and S[i] == "1":
        flip = True
        oneCnt += 1
    elif flip == True and S[i] == "0":
        flip = False

flip = False
zeroCnt = 0

for i in range(len(S)):
    if flip == False and S[i] == "0":
        flip = True
        zeroCnt += 1
    elif flip == True and S[i] == "1":
        flip = False

print(min(oneCnt, zeroCnt))
