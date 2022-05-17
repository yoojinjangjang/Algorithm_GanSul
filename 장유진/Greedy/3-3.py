'''
숫자 카드 게임 : 여러개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임

입력 : N 행 M 열
    : N개의 줄에 걸쳐 각 카드 숫자 주어짐

출력 : 룰에 맞게 선택한 카드 적힌 숫자 출력
'''

n, m = map(int, input().split())
data = []
for i in range(n):
    data.extend(list(map(int,input().split())))

data.sort() #  정렬해서

print(data[n]) # 행 수 번째 인덱스 값이 최소값들 중 최대값


