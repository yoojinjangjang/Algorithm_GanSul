'''
강변에 빌딩들이 옆으로 뺵뺵하게 밀집한 지역이 있다.
이곳에서는 빌딩들이 너무 좌우로 밀집하여, 강에 대한 조망은 모든 세대에서 좋지만
왼쪽 또는 오른쪽 창문을 열었을 때 바로 앞에 옆 건물이 보이는 경우가 허다
하였다.

그래서 이 지역에서는 왼쪽과 오른쪽으로 창문을 열었을 때, 양쪽 모두 거리 2이상의 공간이 확보될 때 조망권이
확보된다고 말한다.
빌딩드렝 대한 정보가 주어질 때, 조망권이 확보된 세대의 수를 반환하는 프로그램을
작성하시오.
'''

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    buildings = list(map(int,input().split()))

    home = 0
    for i in range(2,len(buildings)-2):
        if buildings[i - 1] <= buildings[i] and buildings[i - 2] <= buildings[i] and buildings[i + 1] <= buildings[i] and buildings[i + 2] <= buildings[i]:
            home += buildings[i] - max(buildings[i-1],buildings[i-2],buildings[i+1],buildings[i+2])

    print("#%d %d"%(test_case,home))

