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

# converts the first character of a string to an uppercase letter and all other alphabets to lowercase
def capitalize_string(s: str):
    return s.capitalize()

# replaces the characters from a string, takes 'string', 'old' and 'new' for this operations
def replace_str(s: str, old: str, new: str):
    new_s = s.replace(old, new)
    return new_s

# return the first indesx of a index matching substring
def find_index(s: str, sub: str, ):
    return s.find(sub)

# splits the string using mentioned sepator, return list
def string_split(s: str, separator: str):
    return s.split(separator)
