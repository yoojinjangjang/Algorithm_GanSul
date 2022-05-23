'''
그리디 기출 문제 5. 볼링공 고르기
A 와 B 두 사람이 최대 무게 M인 볼링공 N개에서 서로 무게가 다른 볼링공을 고를 경우의 수
'''
import time

n, k = map(int, input("N, K = ").split())
m = list(map(int,input("볼링공 무게는 : ").split()))

start_time = time.time()
count = 0
temp = m.copy()

for i in m:
    # print("*********************************************")
    # print("현재 리스트 크기 = {}, {}의 개수는 {}".format(len(temp), i, temp.count(i)))
    # print("경우의 수", len(temp) - temp.count(i))

    count += len(temp) - temp.count(i) #현재 배열의 길이에서 자기 자신을 포함한 같은 숫자를 제거한 리스트의 크기가 다른 공과 짝을 이룰 수 있는 경우의 수이다.
    temp.pop(0) #짝을 맞춘 공은 제거해주어서 다음 차례에 같은 쌍이 나오지 않도록 하였다.
    #print("누적 : ",count)
end_time = time.time()
print(count)
print("time : ", end_time-start_time)

'''
start_time =  time.time()
array = [0]*11

for x in m:
    array[x] += 1

result = 0
for i in range(1,k + 1):
    n -= array[i]
    result += array[i]*n

end_time = time.time()
print(result)
print("time : ", end_time-start_time)
'''




