import os

import np


# 1. Iterable משלך שמחזירה מספרים רנדומליים עד לכמות מספרים שנקבעה בבנאי
class RandomNumbersIterable:
    def __init__(self, count):
        self.count = count
        self.current_count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_count < self.count:
            self.current_count += 1
            return np.random.randint(1, 101)
        else:
            raise StopIteration

# שימוש ב-Iterable
random_numbers_iterable = RandomNumbersIterable(5)
for num in random_numbers_iterable:
    print(num)

# 2. פונקציה Generator שמקבלת כתובת לתיקייה במחשב ומחזירה את תוכן כל קובץ בתיקייה
def read_files_in_directory(directory_path):
    for filename in os.listdir(directory_path):
        with open(os.path.join(directory_path, filename), 'r') as file:
            yield file.read()

# 3. בדיקה אם מחרוזת היא Generator
def is_generator(input_str):
    return hasattr(input_str, '__iter__') and not hasattr(input_str, '__getitem__')

# 4. פונקציה Generator המאגדת כמה פונקציות generator אחרות
def combine_generators(gen1, gen2, gen3):
    yield from gen1
    yield from gen2
    yield from gen3

# 5. פונקציה generator שמקבלת מספר ומחזירה כל פעם את המספר + 1
def increment_generator(number):
    while True:
        number += 1
        yield number

# 6. פונקציה generator שמקבלת מספר ומחזירה כל פעם מספר - 1
def decrement_generator(number):
    while True:
        number -= 1
        yield number

# שימוש ב-generator
gen1 = increment_generator(5)
gen2 = decrement_generator(10)
combined_gen = combine_generators(gen1, gen2, read_files_in_directory('.'))
for _ in range(10):
    print(next(combined_gen))
