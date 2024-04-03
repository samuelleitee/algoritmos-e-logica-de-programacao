from array import *

arr = array('u', ['a', 'b', 'c', 'd', 'e'])

print(*arr, sep=' ')

count = 0
for i in arr:
    print('Índice {}: {}'.format(count, i))
    count += 1