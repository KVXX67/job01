def remove_duplicates(lst):
    result = []
    for item in lst:
        found = False
        for existing in result:
            if existing == item:
                found = True
                break
        if not found:
            result.append(item)
    return result

test_list = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
result = remove_duplicates(test_list)
print(result)