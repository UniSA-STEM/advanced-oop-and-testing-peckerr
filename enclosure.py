'''
File: enclosure.py
Description: A brief description of this Python module.
Author: Thomas Cochrane
ID: 110466784
Username: COCTY007
This is my own work as defined by the University's Academic Integrity Policy.
'''

class Enclosure:
    def __init__(self, size: int, environment_type: str, animal_type: str):
        if size < 0:
            raise ValueError('size must be positive')

        self._size = size
        self._environment_type = environment_type
        self._animal_type = animal_type
        self._animals = []
        self._clean_level = 100

    @property
    def size(self):
        return self._size

    @property
    def environment_type(self):
        return self._environment_type

    @property
    def animal_type(self):
        return self._animal_type

    @property
    def animals(self):
        return self._animals

    @property
    def clean_level(self):
        return self._clean_level

    @property
    def animals_housed(self):
        return len(self._animals)

    def is_full(self):
        return self.animals_housed >= self.__size

    def is_liveable(self, animal):
        return self._size == 0



