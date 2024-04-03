from array import array

arr = array('f', [10.5, 20.6, 30.7, 40.8, 50.9])

for i in range(len(arr)):
    print(f'Índice {i} = {arr[i]:.2f}')