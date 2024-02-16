import re
import time
import random
import os
import shutil

import pandas as pd
import json
import openpyxl
import numpy as np

# 1. אמתי כתובת מגורים
def validate_address(address):
    pattern = re.compile(r'^[a-zA-Z\s\d]+,\s\d+,\s[a-zA-Z\s]+$')
    return bool(pattern.match(address))

# 2. אמתי תעודת זהות
def validate_id(id_number):
    pattern = re.compile(r'^\d{9}$')
    return bool(pattern.match(id_number))

# 3. אמתי פונקציה ב-2 נעלמים X ו-Y בלבד
def validate_function(x, y):
    return True if x is not None and y is not None else False

# 4. אמתי תאריך בכל פורמט
def validate_date(date_string):
    try:
        from datetime import datetime
        datetime.strptime(date_string, '%Y-%m-%d')  # הפורמט המבוקש
        return True
    except ValueError:
        return False

# שימוש בפונקציות
print(validate_address("Main St, 123, City"))
print(validate_id("123456789"))
print(validate_function(2, 3))
print(validate_date("2022-01-01"))



#דקורטור
# 1. דקורטור שבודק זמן פעולה
def timi_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.2f} seconds.")
        return result
    return wrapper

# 2. דקורטור שמדפיס "התחלה" ו"סיום" לפני ואחרי פונקציה
def start_end_decorator(func):
    def wrapper(*args, **kwargs):
        print("התחלה")
        result = func(*args, **kwargs)
        print("סיום")
        return result
    return wrapper

# 3. דקורטור ללא משתנים נוספים
def simple_decorator(func):
    def wrapper(*args, **kwargs):
        print("This is a simple decorator.")
        result = func(*args, **kwargs)
        return result
    return wrapper

# שימוש בדקורטורים
@timi_decorator
@start_end_decorator
@simple_decorator
def example_function():
    print("This is an example function.")

example_function()

## הגרלות


# 1. הגרלת מספר בין 0 ל7 - דרך 1
random_number_1 = random.randint(0, 7)

# הגרלת מספר בין 0 ל7 - דרך 2
random_number_2 = random.randrange(8)

# 2. הגרלת 7 מספרים בין 1 ל5 עם RAND5
def rand5():
    return random.randint(1, 5)

def rand7():
    while True:
        num = (rand5() - 1) * 5 + rand5()
        if num <= 21:
            return num % 7 + 1

# שימוש בפונקציה
for _ in range(7):
    print(rand7())



##שגיאות
# 1. פונקציה שמקבלת מחרוזת וטופסת שגיאה מסוימת
def error_function(input_str):
    try:
        number = int(input_str)
    except ValueError:
        raise ValueError("Invalid input. Please enter a valid number.")
    finally:
        print("את תלמידה נהדרת")

# 2. פונקציה שהופכת מחרוזת להפוכה ומדביגה את התרגיל
def reverse_string_and_debug(input_str):
    reversed_str = input_str[::-1]
    print(f"Original String: {input_str}, Reversed String: {reversed_str}")
    return reversed_str

# דוגמאות לשימוש
#error_function("abc")
print(reverse_string_and_debug("Hello, World!"))



##פונקציות נוספות

# 1. בדיקת מספר: נמצא ברשימה, כל הרשימה כמותו, מקסימום, סכום
def check_number_in_list(number, num_list):
    is_in_list = number in num_list
    list_sum = sum(num_list)
    list_max = max(num_list)
    return is_in_list, list_sum, list_max

# 2. קחי 2 רשימות, האחת עם שם הבחור והשניה עם משפחתו והדפיסי אותן בלולאה אחת
def print_names_and_surnames(names, surnames):
    for name, surname in zip(names, surnames):
        print(f"Name: {name}, Surname: {surname}")

# 3. פלטרי רשימת מספרים והשאירי רק מספרים ריבועיים
def filter_square_numbers(numbers):
    return [num for num in numbers if int(num**0.5)**2 == num]

# 4. עבור כל איבר ברשימה החזירי אותו כפול 2 בעזרת ביטים
def double_elements_with_bits(lst):
    return [x << 1 for x in lst]

# 5. עבור רשימת מחבלים, החזירי שמות בשורה אחת
def print_terrorists_names(terrorists):
    names_str = ', '.join(terrorists)
    print(f"Names: {names_str}")

# 6. הפוך מחרוזת של תרגיל להרצה
def reverse_exercise_string(exercise_str):
    reversed_str = exercise_str[::-1]
    return reversed_str

# שימוש בפונקציות
num_list = [1, 2, 3, 4, 5]
print(check_number_in_list(3, num_list))

names = ["John", "Jane", "Bob"]
surnames = ["Doe", "Smith", "Johnson"]
print_names_and_surnames(names, surnames)

numbers = [1, 4, 9, 16, 25]
print(filter_square_numbers(numbers))

original_list = [1, 2, 3, 4]
doubled_list = double_elements_with_bits(original_list)
print(doubled_list)

terrorists_list = ["Mohammed", "Abdul", "Ahmed"]
print_terrorists_names(terrorists_list)

exercise_str = "Hello, World!"
reversed_exercise = reverse_exercise_string(exercise_str)
print(reversed_exercise)


## פונקציות OS SYS



# 1. צרי 3 קבצים, העתיקי 2 מהם ומחקי את השלישי. בכל שלב הדפיסי את המצב.
def create_copy_delete_files():
    file1 = open("file1.txt", "w")
    file1.close()
    file2 = open("file2.txt", "w")
    file2.close()
    file3 = open("file3.txt", "w")
    file3.close()

    print("Files created:", os.listdir("."))

    shutil.copy("file1.txt", "file1_copy.txt")
    shutil.copy("file2.txt", "file2_copy.txt")
    print("Files copied:", os.listdir("."))

    os.remove("file3.txt")
    print("File3 deleted:", os.listdir("."))

#create_copy_delete_files()

# 2. שני את מיקומך ל-2 תיקיות פנימיות וצרי שם תיקיה ריקה ומחקי אותה
def change_location_and_create_empty_directory():
    os.chdir("inner_directory1")
    os.makedirs("empty_directory")
    print("Created inner_directory1 and empty_directory:", os.listdir("."))

    os.chdir("..")  # Go back to the original directory
    os.chdir("inner_directory2")
    os.makedirs("empty_directory")
    print("Created inner_directory2 and empty_directory:", os.listdir("."))

#change_location_and_create_empty_directory()

#קבצים מיוחדים וnumpy קצת...#


# 1. קראי קובץ JSON לתוך מילון והדפיסי רק את הערכים ללא מפתחות
#with open('HtmlTags.json', 'r') as json_file:
#    data = json.load(json_file)
#    values_only = list(data.values())
#    print("Values from JSON file:", values_only)

# 2. צרי קובץ XL , עבור כל אחד מבני משפחתך
data = {
    'Positive Trait': ['Creative', 'Intelligent', 'Energetic'],
    'Talent': ['Musician', 'Writer', 'Athlete'],
    'Age': [25, 30, 22],
    'Distinct Feature': ['Green eyes', 'Curly hair', 'Freckles'],
    'Children': [2, 1, 0]
}

df = pd.DataFrame(data)

with pd.ExcelWriter('family_data.xlsx', engine='openpyxl') as writer:
    writer.book = openpyxl.Workbook()
    df.to_excel(writer, sheet_name='Family Data', index=False)

# 4. הציגי למסך סכום הגילאים
ages_sum = df['Age'].sum()
print("Sum of ages:", ages_sum)

# 5. הציגי למסך איזה צבע שיער מופיע הכי הרבה פעמים
hair_color_counts = df['Distinct Feature'].value_counts()
most_common_hair_color = hair_color_counts.idxmax()
print("Most common hair color:", most_common_hair_color)

# 6. הציגי למסך כמה נכדים להוריך
grandchildren_count = df[df['Children'] > 0]['Children'].sum()
print("Number of grandchildren:", grandchildren_count)

# 7. מהו הגיל הממוצע של האחים?
average_parents_age = df[df['Children'] > 0]['Age'].mean()
print("Average age of parents:", average_parents_age)

# 8. אנא מלא את הגיל הממוצע במקומות החסרים.
df['Age'].fillna(df['Age'].mean(), inplace=True)

# 9. מהו אחוז הילדים שנולדו לפניך?
your_children_percentage = (df[df['Age'] > 0]['Children'].sum() / df['Children'].sum()) * 100
print("Percentage of children born before you:", your_children_percentage)

# 10. כמה אחוז מהילדים (גיל 12 ומטה) הצליחו לשרוד?
children_survival_percentage = (df[df['Age'] <= 12]['Children'].sum() / df['Children'].sum()) * 100
print("Percentage of children who survived (age 12 and below):", children_survival_percentage)

# 11. איזו אות מופיעה הכי הרבה בתחביבים?
hobbies_str = ', '.join(df['Talent'])
most_common_letter = pd.Series(list(hobbies_str)).mode()[0]
print("Most common letter in hobbies:", most_common_letter)

# 12. צור מערך דו-מימדי ומלא אותו באופן אקראי 1-8
random_matrix = np.random.randint(1, 9, size=(3, 5))
print("Random 2D array:")
print(random_matrix)

# 13. עבור כל תא חשבי את ממוצע התאים עד אליו מהפינה השמאלית עליונה
cumulative_avg_matrix = np.cumsum(random_matrix, axis=1) / np.arange(1, random_matrix.shape[1] + 1)
print("Cumulative average matrix:")
print(cumulative_avg_matrix)

# 14. צור מערך חד-מימדי ומיין אותו באיזה מיון שתבחר
sorted_array = np.sort(random_matrix.flatten())
print("Sorted 1D array:")
print(sorted_array)


##איטרטור וגנרטור
