
#create a list/array
listx= [35,33,44,10,44,19,27,44,26,31]
listy = [67,45,32,00,100]

#traverse
def traverse():
    for i in listx:
        print(i)

#insert
def insert():

    listx.append(30)
    return listx

#copy
def copy_list():
    second = listx.copy()
    return second

def extend_list():
    extended = listx.extend(listy)
    return listx

def insert_new():
    listy.insert(2,90)
    return listy

def pop_list():
    popped = listy.pop(-2)
    return popped

def counting():
    counted= listx.count(44)
    return counted

def indexes():
    indexed = listx.index(44)
    return indexed

def remove_stuff():
    listx.remove(44)
    return listx

def clear_list():
    listy.clear()
    return listy

def reverse_list():
    listy.reverse()
    return listy

def sort_x():
    listy.sort()
    return listy

output = sort_x()
print (output)