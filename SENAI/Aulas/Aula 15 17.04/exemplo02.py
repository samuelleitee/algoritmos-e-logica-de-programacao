from array import *

arr = array('i', [10, 20, 30, 40, 50])

print(arr)

count = 0
for i in arr:
    print('Índice {}: {}'.format(count, i))
    count += 1