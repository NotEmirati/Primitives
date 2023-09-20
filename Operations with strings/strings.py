# joins elements with ' ' into one string
def joinString(s:str):
    phrase = ' '.join(s)
    return phrase

# removes characters from the string
def removechar(string):
    chars = 'AEIOUaeiou'
    result = ''
    for chars in string:
        if chars not in chars:
          result += chars
    print(removechar('lorem ipsum'))
    return result
    



