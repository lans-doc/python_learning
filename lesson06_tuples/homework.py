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

def statistics(*numbers):
    if not numbers:
        return None

    min_number = numbers[0]
    max_number = numbers[0]

    for n in numbers[1:]:
        if n > max_number:
            max_number = n
        if n < min_number:
            min_number = n

    return min_number, max_number, (sum(numbers)/len(numbers))

def second_maximum(*numbers):
    if not numbers:
        return None
    
    maximum = numbers[0]
    second = numbers[0]

    for n in numbers[1:]:
        if n > maximum:
            second = maximum
            maximum = n
        if (n < maximum and n > second) or second == maximum:
            second = n

    if second == maximum:
        return None

    return second
