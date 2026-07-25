def maximum(*numbers):
    if not numbers:
        return None
    else:
        max_number = numbers[0]
        for n in numbers:
            if n > max_number:
                max_number = n
        return max_number

print(maximum(5, 55, 65, 34))