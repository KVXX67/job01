def find_min_max():
    L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
    min_val = L[0]
    max_val = L[0]
    for num in L:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    return min_val, max_val

min_val, max_val = find_min_max()
print(min_val)
print(max_val)