def sum_all(*numbers):
    sum = 0
    for n in numbers:
        sum += n

    return sum   

def average(*numbers):
    if len(numbers):
        return (sum(numbers)/len(numbers))
    else:
        return "empty"

print(average())