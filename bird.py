'''
File: bird.py
Description: A brief description of this Python module.
Author: Thomas Cochrane
ID: 110466784
Username: COCTY007
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal

class Bird(Animal):
    def __init__(self, name, species, age, dietary_needs, environmental_type):
        super().__init__(name, species, age, dietary_needs, environmental_type)

    def make_sound(self) -> str:
        return f'{self._name} makes a bird noise'

    def get_category(self):
        return 'Bird'

    def fly(self):
        return f'{self._name} flaps it\'s wings.'