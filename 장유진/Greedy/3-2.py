'''
큰 수의 법칙 : 다양한 수로 이루어진 배열을 M번 더하여 가장 큰 수를 만드는 법칙 ( 배열의 특정 수가 K번 연속 더해질 수 없다.)

입력 : N M K
     N개의 자연수
출력 : 큰 수의 법칙에 따른 답
'''

n, m, k = map(int, input().split())

numbers = list(map(int,input().split()))
ans = 0

numbers.sort()

i = m//(k+1) # 순열의 반복 횟수
ans = i*k*numbers[n-1] # 큰수의 합
ans += i*numbers[n-2] # 두번째로 큰수의 합
ans += (m%(k+1))*numbers[n-1] # 남은 큰수의 합

print(ans)
