import sys

pos = sys.stdin.readline()
result = 0

if ord(pos[0]) < ord("b") or ord(pos[0]) > ord("g"):
    if int(pos[1]) < 2 or int(pos[1]) > 7:
        result = 2
    elif int(pos[1]) < 3 or int(pos[1]) > 6:
        result = 3
    else:
        result = 4
elif ord(pos[0]) < ord("c") or ord(pos[0]) > ord("f"):
    if int(pos[1]) < 2 or int(pos[1]) > 7:
        result = 3
    elif int(pos[1]) < 3 or int(pos[1]) > 6:
        result = 4
    else:
        result = 6
else:
    if int(pos[1]) < 2 or int(pos[1]) > 7:
        result = 4
    elif int(pos[1]) < 3 or int(pos[1]) > 6:
        result = 6
    else:
        result = 8

print(result)
