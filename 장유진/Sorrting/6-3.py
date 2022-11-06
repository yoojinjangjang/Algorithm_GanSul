'''
삽입 정렬
'''

array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(array)):
    for j in range(i-1,-1,-1):
        if array[j] > array[j+1]:
            array[j],array[j+1] = array[j+1],array[j]
print(array)

array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(array)):
    for j in range(i-1,-1,-1):
        if array[j+1] < array[j]:
            array[j+1],array[j] = array[j], array[j+1]
print(array)