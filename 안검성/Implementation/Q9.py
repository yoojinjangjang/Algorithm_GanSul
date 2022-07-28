import sys


def string_compress(s):
    compress_len = len(s)
    for i in range(1, len(s) // 2 + 1):
        compressed = ""
        compressing = s[0:i]
        cnt = 1
        for j in range(i, len(s), i):
            if compressing == s[j : j + i]:
                cnt += 1
            else:
                if cnt > 1:
                    compressed += str(cnt) + compressing
                else:
                    compressed += compressing
                compressing = s[j : j + i]
                cnt = 1
        if cnt > 1:
            compressed += str(cnt) + compressing
        else:
            compressed += compressing
        compress_len = min(compress_len, len(compressed))
    return compress_len


s = sys.stdin.readline()
print(string_compress(s))
