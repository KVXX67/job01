def swap_first_last(lst):
    if len(lst) < 2:
        return lst
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst

test_list = [1, 2, 3, 4, 5]
result = swap_first_last(test_list.copy())
print(result)