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