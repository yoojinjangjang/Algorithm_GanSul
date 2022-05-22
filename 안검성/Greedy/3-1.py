N = 1260

coin_types = [500, 100, 50, 10]
coin_cnt = 0

for i in coin_types:
    coin_cnt += N // i
    N %= i

print(coin_cnt)
