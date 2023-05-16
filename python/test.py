array = [5, 4, 3, 2, 1]
current = array[0]

if array[0] > array[1]:
    sliced = array.pop(1)
    print(sliced)
    print(array)
