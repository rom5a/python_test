def search_number_near_zero(numbers):
    minimal = numbers[0]
    for number in numbers:
        if (abs(number) <= abs(minimal) and number > minimal) or number == 0:
            minimal = number
    return minimal


nums = (-1, 2, 1, -2)
result = search_number_near_zero(nums)
print(result)
