def sum_even_values():
    L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]
    total = 0
    for num in L:
        if num % 2 == 0:
            total += num
    return total

result = sum_even_values()
print(result)