def solution(s):
    for i in range(1, len(s)//2 +1):
        result = ''
        temp_str = s[0:i]
        cnt = 1
        for j in range(i, len(s), i):
            if temp_str == s[j:j + i]:
                cnt += 1
            else: 
                result += str(cnt) + temp_str if cnt >= 2 else temp_str
                temp_str = s[j:j + i]
                cnt = 1

    return len(result)

if __name__ == "__main__":
    print(solution("aabbaccc")) #7 2a2ba3c
    print(solution("ababcdcdababcdcd")) #9
    print(solution("abcabcdede")) #8
    print(solution("abcabcabcabcdededededede")) # 14
    print(solution("xababcdcdababcdcd")) #17
