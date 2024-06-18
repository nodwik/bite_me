NOT_FOUND = "Not found"

group1 = {'tim': 30, 'bob': 17, 'ana': 24}
group2 = {'ana': 26, 'thomas': 64, 'helen': 26}
group3 = {'brenda': 17, 'otto': 44, 'thomas': 46}


def get_person_age(name):
    """Look up name (case insensitive search) and return age.
       If name in > 1 dict, return the match of the group with
       greatest N (so group3 > group2 > group1)
    """
    name = str(name).lower()

    if name is None:
        return NOT_FOUND
    elif name is False:
        return NOT_FOUND

    my_dict = [group1, group2, group3]
    found_age = []
    for group in reversed(my_dict):
        lower_group = {k.lower(): v for k, v in group.items()}
        if name in lower_group:
            found_age.append(lower_group[name])

    if len(found_age) >= 1:
        return found_age[0]
    else:
        return NOT_FOUND

result = get_person_age(-1)
print(result)