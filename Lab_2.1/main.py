def search_number_near_zero(numbers):
    minimal = numbers[0]
    for number in numbers:
        if (abs(number) <= abs(minimal) and number > minimal) or number == 0:
            minimal = number
    return minimal


def open_file(file_name):
    array = []
    with open(file_name) as f:
        for line in f:
            array.append([int(x) for x in line.split()])
    return array


nums = open_file('number.txt')
#print(nums)

for row in nums:
    result = search_number_near_zero(row)
    print(result)
