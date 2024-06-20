IGNORE_CHAR = 'b'
QUIT_CHAR = 'q'
MAX_NAMES = 5



# def filter_names(names):
#     return_list = []
#     count_names = 0
#     for name in names:
#         if name[0] == IGNORE_CHAR:
#             continue
#         elif name[0] == QUIT_CHAR:
#             break
#         else:
#             digits = 0
#             for char in name:
#                 if char.isdigit():
#                     digits += 1
#             if digits > 0:
#                 continue
#             else:
#                 if count_names == MAX_NAMES:
#                     break
#                 else:
#                     count_names += 1
#                     return_list.append(name)
#     return return_list


def filter_names(names):
    return_list = []
    count_names = 0

    for name in names:
        if name[0] == IGNORE_CHAR:
            continue
        if name[0] == QUIT_CHAR:
            break
        if any(char.isdigit() for char in name):
            continue

        return_list.append(name)
        count_names += 1

        if count_names == MAX_NAMES:
            break

    return return_list