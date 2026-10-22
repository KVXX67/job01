def round_number(num):
    integer_part = int(num)
    fractional_part = num - integer_part
    if num < 0:
        if fractional_part <= -0.5:
            return integer_part - 1
        else:
            return integer_part
    else:
        if fractional_part >= 0.5:
            return integer_part + 1
        else:
            return integer_part

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

def process_numbers():
    numbers = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]
    rounded_numbers = []
    for num in numbers:
        rounded_numbers.append(round_number(num))
    sorted_numbers = sort_list(rounded_numbers)
    return sorted_numbers

result = process_numbers()
print(result)