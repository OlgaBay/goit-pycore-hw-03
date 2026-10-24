import random


def get_numbers_ticket(min, max, quantity) -> list[int]:    
    # Генерує відсортований список унікальних випадкових чисел 
    # Повертає порожній список, якщо параметри некоректні

    if min < 1 or max > 1000:
        return []
    elif quantity < 1:
        return []
    elif min > max:
        return []
    elif quantity > (max - min + 1):
        return []
    else:
        numbers = random.sample(range(min, max + 1), quantity)
        numbers.sort()
        return numbers
    
try:
    min = int(input("Bведіть мінімальне число: "))
    max = int(input("Bведіть максимальне число: "))
    quantity = int(input("Введіть кількість лотерейних номерів: "))

    result = get_numbers_ticket(min, max, quantity)

    if not result:
        print("Ви ввели некоректні дані")
    else:
        print(f"Ваші лотерейні числа: {result}")

except ValueError:
    print("Ви ввели некоректні дані")