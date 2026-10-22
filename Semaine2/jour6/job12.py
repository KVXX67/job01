def sort_list(lst):
    result = lst[:]
    n = 0
    for _ in result:
        n += 1
    for i in range(n):
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
    return result

test_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = sort_list(test_list)
print(sorted_list)