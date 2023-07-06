import random

class Human:
    """Наш первый класс"""
    genom_count = 46

    def __init__(self, name, age, discription):
        self.name = name
        self.age = age
        self.discription = discription

    def show_description(self):
        print(self.name, self.discription, self.age)

    @classmethod
    def get_genom_count(cls):
        return cls.genom_count

    @classmethod
    def set_genom_count(cls, count: int):
        cls.genom_count = count

    @staticmethod
    def choice_name():
        return random.choice(('Andrew', 'Timur', 'Ivan', 'Artem'))


human = Human('Andrew', 17, 'hui')
print(human.choice_name())
