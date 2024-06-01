def count_indents(text: str) -> int:
    """
    Count and return the number of leading white space characters (' ').
    """
    leading_space = []
    for char in text:
        if char == ' ':
            leading_space.append(char)
        else:
            break
    return len(leading_space)

# different solution
'''
The takewhile function takes two arguments:

	1.	A predicate function: This is a function that returns True or False for a given input. In your example, lambda x: x == ' ' is the predicate function.
	2.	An iterable: This is the sequence of items you want to process, in your case, text.

The takewhile function creates an iterator that yields items from the iterable as long as the predicate function returns True. As soon as the predicate function returns False for an item, takewhile stops iterating.

'''
from itertools import takewhile
leading_space = [space for space in takewhile(lambda x: x == ' ', text)]
