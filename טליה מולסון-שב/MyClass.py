# 1. מחלקה עם 3 משתנים
class MyClass:
    class SlotMachine:
        def __init__(self, private=1, protected=2, public=3, name="Default Slot", theme="Default Theme", paylines=3,bet=1, jackpot=1000):
            self.__private = private
            self._protected = protected
            self.public = public
            self.name = name
            self.theme = theme
            self.paylines = paylines
            self.bet = bet
            self.jackpot = jackpot

    # 2. GET ו-SET
    def get_private(self):
        return self.__private

    def set_private(self, value):
        self.__private = value

    # 3. פרופרטיז על ידי דיזיין פטרנס
    @property
    def protected(self):
        return self._protected

    @protected.setter
    def protected(self, value):
        self._protected = value

    # 4. פונקציה סטטית
    @staticmethod
    def static_function():
        print("This is a static function")

# 5. שימוש במחלקה
obj = MyClass()
#print(obj.get_private())  # גישה למשתנה פרטי באמצעות פונקציה
obj.set_private(10)  # שינוי ערך למשתנה פרטי באמצעות פונקציה
#print(obj.protected)  # קריאה לפרופרטי protected
obj.protected = 20  # שינוי ערך לפרופרטי protected
#print(obj.static_function())  # קריאה לפונקציה סטטית

# 6. ירושה מ-OBJECT ודריסת פונקציות
class MyDerivedClass(MyClass):
    def __init__(self, private, protected, public, additional):
        super().__init__(private, protected, public)
        self.additional = additional

    # דריסת פונקציה מהמחלקה ההורשה
    def static_function(self):
        print("Overridden static function")

# דוגמה לשימוש במחלקה שירשה מ-OBJECT
derived_obj = MyDerivedClass(1, 2, 3, 4)
print(derived_obj.static_function())  # קריאה לפונקציה מהמחלקה המורשה




# יצירת סלוטים
slot1 = MyClass(name="Fruit Slot", theme="Fruit", paylines=3, bet=1, jackpot=1000)
slot2 = MyClass(name="Adventure Slot", theme="Adventure", paylines=5, bet=2, jackpot=5000)
slot3 = MyClass(name="Egyptian Slot", theme="Ancient Egypt", paylines=10, bet=5, jackpot=10000)
slot4 = MyClass(name="Wild West Slot", theme="Wild West", paylines=3, bet=1, jackpot=1500)
slot5 = MyClass(name="Underwater Slot", theme="Underwater", paylines=20, bet=10, jackpot=20000)