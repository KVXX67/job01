def product_in_range():
    L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
    product = 1
    found = False
    for num in L:
        if 25 <= num <= 90:
            product *= num
            found = True
    if not found:
        return 0
    return product

result = product_in_range()
print(result)