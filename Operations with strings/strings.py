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

# return f-string using input
def f_string(name: str, age: int, occupation: str):
    if age < 18:
        return 'You are not allowed'
    else:
        return f'Hello {name}, I see you were born {age} years ago and your occupation is a/an {occupation}'

# slices the string
def string_slice(s: str, b: int, e: int):
    slice1 = s[:]
    slice2 = s[b:e]
    slice3 = s[b:]
    slice4 = s[:e]
    return f'{slice1}\n{slice2}\n{slice3}\n{slice4}'

# converts string to uppercase
def upper_case_string(s: str):
    return s.upper()
    
# converts string to lowercase
def lower_case_string(s: str):
    return s.lower()
