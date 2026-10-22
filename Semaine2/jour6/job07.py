def count_multiples_of_three():
    L = [8, 24, 48, 2, 16]
    count = 0
    for num in L:
        if num % 3 == 0:
            count += 1
    return count

result = count_multiples_of_three()
print(result)