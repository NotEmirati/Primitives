# joins elements with ' ' into one string
def joinString(s:str):
    phrase = ' '.join(s)
    return phrase

# removes characters from the string
def removechar(string: str):
    chars: str = 'AEIOUaeiou'
    result: str = ''
    for char in string:
        if char not in chars:
          result += char
    return result
    # test code: print(removechar('lorem ipsum'))    





