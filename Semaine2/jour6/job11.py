def increment_list_elements():
    L = [7, 11, 42, 39, 2]
    for i in range(len(L)):
        L[i] += 1
    return L

result = increment_list_elements()
print(result)