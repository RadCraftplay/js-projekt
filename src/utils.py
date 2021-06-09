def flatmap(array):
    ret_val = []

    for top_element in array:
        for lower_element in array:
            ret_val.append(lower_element)

    return ret_val
