def linearSearch(listx, x):
    
    for index, element in enumerate(listx):
        if x == element:
            return index

    return -1


if __name__ == "__main__":
    array = [2, 4, 0, 1, 9]
    x = 4

    result = linearSearch(array, x)
    print(result)


    
    