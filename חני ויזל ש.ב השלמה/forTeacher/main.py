from MyClass import MyClass
from MySubclass import MySubclass
import re
from datetime import datetime
import time
import random
from RandomNumbers import RandomNumbers

def TIMI(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time for {func.__name__}: {end_time - start_time} seconds")
        return result
    return wrapper


def print_start_end(func):
    def wrapper(*args, **kwargs):
        print(f"התחלה של {func.__name__}")
        result = func(*args, **kwargs)
        print(f"סיום של {func.__name__}")
        return result
    return wrapper

def validate_address(address):
    pattern = r'^[\u0590-\u05FF\s]+ בית \d+ דירה \d+$'
    if re.match(pattern, address):
        print("הכתובת תקינה.")
    else:
        print("הכתובת אינה תקינה.")


validate_address("רחוב הראשונים בית 1 דירה 5")

@TIMI
@print_start_end
def validate_id(id_number):

    if len(id_number) != 9:
        return False

    if not re.match(r'^\d{9}$', id_number):
        return False

    if int(id_number[0]) == 0 or int(id_number[0]) == 9:
        return False

    sum = 0
    for i in range(0, 9):
        digit = int(id_number[i])
        if i % 2 == 0:
            sum += digit
        else:
            double = digit * 2
            sum += (double // 10) + (double % 10)

    if sum % 10 == 0:
        return True
    else:
        return False


id_number_to_check = "132456789"

if validate_id(id_number_to_check):
    print("תעודת הזהות תקינה.")
else:
    print("תעודת הזהות אינה תקינה.")

@TIMI
@print_start_end
def validate_date(date_string):
    try:
        datetime.strptime(date_string, '%Y-%m-%d')
        return True
    except ValueError:
        return False


if validate_date("2024-02-15"):
    print("התאריך תקין.")
else:
    print("התאריך אינו תקין.")




obj = MyClass()
print("Public variable:", obj.public_var)
print("Protected variable:", obj.protected_var)
print("Private variable:", obj.get_private_var())

obj.set_private_var(10)
print("Modified private variable:", obj.get_private_var())

obj.protected_var = 20
print("Modified protected variable:", obj.protected_var)

print(MyClass.static_function())
obj2 = MySubclass(4, 5, 6)
obj2.set_private_var(100)
print("Modified private variable in subclass:", obj2.get_private_var())

obj2.static_function()

random_number = random.randint(0, 7)
print(random_number)

random_number = random.randrange(0, 8)
print(random_number)
num = 5
lst = [1, 2, 3, 4, 5, 6]

result = (num in lst, all(element == num for element in lst), max(lst), sum(lst))
print(result)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squared_numbers = list(filter(lambda x: x**0.5 == int(x**0.5), numbers))

print(squared_numbers)

random_iter = RandomNumbers(5)


for num in random_iter:
    print(num)