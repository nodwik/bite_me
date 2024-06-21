from typing import Union


def fizzbuzz(num: int) -> Union[str, int]:
    if num % 3 == 0 and num % 5 == 0:
        return 'Fizz Buzz'
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    else:
        return num

print(fizzbuzz(23))

# another possibility:

from typing import Union

def fizzbuzz2(num: int) -> Union[str, int]:
    result = ""
    if num % 3 == 0:
        result += "Fizz"
    if num % 5 == 0:
        result += "Buzz"
    return result if result else num