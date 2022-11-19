'''
퀴즈 대회에 참가해서 우승을 하게 되면
보서느 상금을 휙득할 수 있는 기회를 부여 받는다. 우승자는 주어진 숫자판들 중에 두 개를 선택에서
정해진 횟수만큼 서로의 자리를 위치를 교환할 수 있다.

정해진 횟수만큼 교환이 긑나면 숫자판의 위치에 부여된 가중치에 의해 상금이 계산된다.
숫자판의 오른쪽 끝에서부터 1원이고 왼쪽으로 한자리씩 갈수록 10의 배수만큼 커진다.

반드시 횟수만큼 교환이 이루어져야 하고 동일한 위치의 교환이 중복되어도 된다.

'''


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    numbers, rotation_cnt = input().split()
    rotation_cnt = int(rotation_cnt)
    numbers = list(map(int,list(numbers.strip())))
    for i in range(rotation_cnt):

