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

# returns cleared list
def clear_list(l: list):
    l.clear()
    return l
# copies new_list from old_list
def copy_list(old_list: list, new_list: list):
    new_list = old_list.copy()
    return new_list

# sorts the list in reversed order, option 1. Doesn't support 'key' and 'reverse' args.
def sorted_list(old_list: list):
    new_list = sorted(old_list)
    return new_list

# sorts the list in reversed order, option 2. Doesn't support 'key' and 'reverse' args.
def sort_list(l: list):
    l.sort()
    return l

# reverses the list
def reverse_list(l: list):
    l.reverse()
    return l

# counts the number of times the integer element appears in the list
def count(l: list, e: int):
    return l.count(e)
