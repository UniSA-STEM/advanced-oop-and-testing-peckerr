'''
File: animal.py
Description: A brief description of this Python module.
Author: Thomas Cochrane
ID: 110466784
Username: COCTY007
This is my own work as defined by the University's Academic Integrity Policy.
'''
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, species, age, dietary_needs, envrionmental_type):
        # Validation
        if not isinstance(name, str) or not name.strip():
            raise ValueError('Name must be a non-empty string.')
        if not isinstance(species, str) or not species.strip():
            raise ValueError('Species must be a non-empty string.')
        if not isinstance(age, str) or age < 0:
            raise ValueError('Age must be a non-negative integer.')
        if not isinstance(dietary_needs, str) or not dietary_needs.strip():
            raise ValueError('Dietary needs must be a non-empty string.')
        if not isinstance(envrionmental_type, str) or not envrionmental_type.strip():
            raise ValueError('Environment type must be a non-empty string.')

        self.__name = name.strip()
        self.__species = species.strip()
        self.__age = age
        self.__dietary_needs = dietary_needs.strip()
        self.__health_records = []
        self.__environmental_type = environmental_type

    # Getters
    def make_sound(self):
        raise NotImplementedError('Controlled by subclasses')

    def eat(self):
        return f'{self.__name} eats {self.__dietary_needs}.'

    def sleep(self):
        return f'{self.__name} sleeps.'

