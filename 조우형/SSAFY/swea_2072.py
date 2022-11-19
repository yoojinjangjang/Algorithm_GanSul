'''
SWEA 2072.
10개의 수를 입력 받아, 그 중에서 홀수만 더한 값을 출력하는 프로그램을 작성하라.
'''
t = int(input())
numbers = []
sum_List = []
for i in range(t):
    numbers.append(list(map(int, input().split(" "))))

for number in numbers:
    sum = 0
    for n in number:
        if n%2 == 1:
            sum += n
    sum_List.append(sum)
idx = 1
for s in sum:

    print("#{} {}".format(idx, s))
    idx += 1



T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):




    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////////////////////////////
