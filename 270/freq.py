# def freq_digit(num: int) -> int:
#     my_dict = {}
#     result = (0, 0)
#
#     for nr in str(num):
#         if nr in my_dict.keys():
#             my_dict[nr].append(nr)
#         else:
#             my_dict[nr] = [nr]
#     for key, value in my_dict.items():
#         if len(value) > result[0]:
#             result = (len(value), int(key))
#     print(result[1])
#     print(my_dict)
#     return result[1]


def freq_digit(num: int) -> int:
    """
    Finds the most frequent digit in a given integer.

    Parameters:
    num (int): The input number.

    Returns:
    int: The digit that appears most frequently in the input number.
    """
    my_dict = {}

    # Count occurrences of each digit
    for nr in str(num):
        if nr in my_dict:
            my_dict[nr] += 1
        else:
            my_dict[nr] = 1

    # Find the digit with the maximum count
    max_count = 0
    max_digit = 0
    for key, value in my_dict.items():
        if value > max_count:
            max_count = value
            max_digit = int(key)

    return max_digit

freq_digit(994145467)