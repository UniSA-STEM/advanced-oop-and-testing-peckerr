'''
File: enclosure.py
Description: A brief description of this Python module.
Author: Thomas Cochrane
ID: 110466784
Username: COCTY007
This is my own work as defined by the University's Academic Integrity Policy.
'''

class Enclosure:

    ENVIRONMENTS = ['Aquatic', 'Tropical', 'Snow', 'Desert', 'Jungle']

    def __init__(self, enclosure_name, size, environment_type, clean_level):
        if not isinstance(enclosure_name, str):
            raise ValueError('Enclosure name must be a string.')
        if not isinstance(size, int) or size < 0:
            raise ValueError('Enclosure size must be a positive integer.')
        if environment_type not in self.ENVIRONMENTS:
            raise ValueError(f'Enclosure environment type must be one of: {self.ENVIRONMENTS}')
        if not isinstance(clean_level, int) or not 0 <= clean_level <= 100:
            raise ValueError('Clean level must be an integer between 0 and 100.')

        self._enclosure_name = enclosure_name
        self._size = size
        self._environment_type = environment_type
        self._clean_level = clean_level
        self._animals = []
        self._allowed_species = None

    @property
    def enclosure_name(self):
        return self._enclosure_name

    @property
    def size(self):
        return self._size

    @property
    def environment_type(self):
        return self._environment_type

    @property
    def cleanliness_level(self):
        return self._clean_level

    @property
    def animals(self):
        return self._animals.copy()

    @property
    def animal_count(self):
        return len(self._animals)

    def add_animal(self, animal):
        if animal.environment_type != self._environment_type:
            raise ValueError(f'{animal.name} needs to be in the {self._environment_type} enclosure.')

        if self._allowed_species is None:
            self._allowed_species = animal.species
        elif animal.species != self._allowed_species:
            raise ValueError(f'{animal.species} cannot mix with {self._allowed_species}.')
        self._animals.append(animal)
        return True

    def remove_animal(self, animal):
        if animal in self._animals:
            self._animals.remove(animal)
            if len(self._animals) == 0:
                self._animals = None
            return True
        return False

    def clean(self):
        self._clean_level = 100
        return f'Enclosure {self._enclosure_name} has been cleaned.'

    def __str__(self):
        return f'Enclosure {self._enclosure_name}({self._environment_type}) contains {len(self._animals)} animals.'

