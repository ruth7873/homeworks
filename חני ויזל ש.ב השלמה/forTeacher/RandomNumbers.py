import random

class RandomNumbers:
    def __init__(self, count):
        self.count = count
        self.generated = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.generated < self.count:
            self.generated += 1
            return random.randint(0, 100)
        else:
            raise StopIteration


