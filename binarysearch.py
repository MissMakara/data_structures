
def iterativeBinarySearch(array, x):

    low= 0
    high = (len(array)-1)

    while low < high:
        mid = low + ((high - low)//2)

        if array[mid] == x:
            return mid

        elif array[mid] < x:
            low = mid +1
        
        elif array[mid] > x:
            high = mid - 1
    return -1


def recursiveBinarySearch(array, x):
    low = 0
    high = (len(array)-1)

    while high >= low:
        mid = low + (high-low)//2

        if array[mid] == x:
            return mid

        elif array[mid] > x:
            high = mid-1
            array_y= []
            for i in range(low, high):
                array_y.append(array[i])

            recursiveBinarySearch(array_y, x)

        elif array[mid] < x:
            low = mid + 1
            array_y = []
            for i in range(low, high):
                array_y.append(array[i])

            recursiveBinarySearch(array_y, x)

    return -1





array = [3, 4, 5, 6, 7, 8, 9]
x = 8

result = recursiveBinarySearch(array, x)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")



