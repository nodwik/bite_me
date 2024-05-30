VOWELS = 'aeiou'
PYTHON = 'python'


#def contains_only_vowels(input_str):
#    """Receives input string and checks if all chars are
#       VOWELS. Match is case insensitive."""
#    return len(input_str) == len([char for char in input_str.lower() if char in 'aeiou'])


#def contains_any_py_chars(input_str):
#    """Receives input string and checks if any of the PYTHON
#       chars are in it. Match is case insensitive."""
#    return len([char for char in input_str.lower() if char in 'python']) > 0


#def contains_digits(input_str):
#    """Receives input string and checks if it contains
#       one or more digits."""
#    return len([char for char in input_str.lower() if char in '0123456789']) > 0


# generator expressions:
# (expression for item in iterable if condition)

def contains_only_vowels(input_str):
    """Receives input string and checks if all chars are
       VOWELS. Match is case insensitive."""
    return all(char.lower() in 'aeiou' for char in input_str)


def contains_any_py_chars(input_str):
    """Receives input string and checks if any of the PYTHON
       chars are in it. Match is case insensitive."""
    return any(char.lower() in 'python' for char in input_str)


def contains_digits(input_str):
    """Receives input string and checks if it contains
       one or more digits."""
    return any(char.isdigit() for char in input_str)




result = contains_only_vowels('asshole')
print(result)

result2 = contains_any_py_chars('physik')
print(result2)

result3 = contains_digits('phys1k')
print(result3)