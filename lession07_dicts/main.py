students = {"name": "Alex", "address": {"city": "Venna", "street": "Heminguy 12"}}

print(students["address"]["city"])

def even_squares(*numbers):
    return [n * n for n in numbers if n % 3 == 0]

print(even_squares(3, 4, 5, 6, 7, 8, 9, 3))