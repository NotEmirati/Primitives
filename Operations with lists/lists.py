listName = [1, 2, 3, 4, 5]

#sums all elements in the list
def sumList(listName):
  return sum(listName)

#adds an element to the list
def appendList(n:int):
    listName.append(n)
  
#extends the list with another list and a tuple
def extendList(l: list, t: tuple):
    listName.extend(l)
    listName.extend(t)

#inserts the elements with specific index
def insertList(l: list):
    l.insert(2, 'a')
    return l

#removes elemetn of a list based on it's index
def removeItem(l: list):
    l.pop(1)
    return l

#returns index of an element from the list using the following 
def index_element(userlist: list, value, start, stop):
    try:
        return userlist.index(value, start, stop)
    except ValueError:
        return 'Item is not in the list or range'

# return square value
def square(n):
    return n*n

def square_list(function, l: list):
    return list(map(square, l))

def square_with_lambda(l: list):
    return list(map(lambda x: x*x, l))

# list slicing
def slice_list(l: list, b: int, e: int):
    slice1 = l[:]
    slice2 = l[b:e]
    slice3 = l[b:]
    slice4 = l[:e]
    return f'{slice1}\n{slice2}\n{slice3}\n{slice4}'


