balance = 1260
list = [500,100,50,10]
n =0;

for i in list:

    n += balance//i
    balance = balance - (balance//i)*i

print(n) 