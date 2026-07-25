def sum_all(*numbers):
    sum = 0
    for n in numbers:
        sum += n

    return sum   

print(sum_all(1, 3, 5))