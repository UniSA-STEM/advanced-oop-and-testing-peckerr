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

        self.__size = size
        self.__environment_type = environment_type
        self.__animal_type = animal_type
        self.__animals = []
        self.__clean_level = 100

