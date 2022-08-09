#A program that checks if there are duplicate values in a dictionary

def check_for_dict_duplicate_values(diction: dict)->str:
    v = diction.values()

    v_set = set(v)

    if len(v) == len(v_set):
        return "there are no duplicates among the values "
    return "there are duplicates among the values"
