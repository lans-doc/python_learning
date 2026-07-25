def maximum(*numbers):
    if not numbers:
        return None
    else:
        max_number = numbers[0]
        for n in numbers:
            if n > max_number:
                max_number = n
        return max_number

def minimum(*numbers):
    if not numbers:
        return None

    min_number = numbers[0]
    for n in numbers[1:]:
        if n < min_number:
            min_number = n
        return min_number

print(minimum(5, 55, 65, 34))