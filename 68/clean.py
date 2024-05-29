import re
def remove_punctuation(input_string):
    """Return a str with punctuation chars stripped out"""
    #return re.sub(r'[!"#$%&\'()*+,-./:;<=>?@[\\\]^_`{|}~]', '', input_string)
    mlist = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    return ''.join([char for char in input_string if char not in mlist])


input_str = "Hello, world! How's it going?"
result = remove_punctuation(input_str)
print(result)  # Output: "Hello world Hows it going"

