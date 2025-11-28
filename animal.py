'''
File: animal.py
Description: A brief description of this Python module.
Author: Thomas Cochrane
ID: 110466784
Username: COCTY007
This is my own work as defined by the University's Academic Integrity Policy.
'''

from abc import ABC, abstractmethod
from datetime import datetime

class Animal(ABC):
    def _init_(self, name, species, age, dietary_needs, envrionmental_type):
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

        self._name = name.strip()
        self._species = species.strip()
        self._age = age
        self._dietary_needs = dietary_needs.strip()
        self._health_records = []
        self._environmental_type = environmental_type
        self._at_vet = False
        self._last_fed = None

    # Properties for getters
    @property
    def name(self):
        return self._name

    @property
    def species(self):
        return self._species

    @property
    def age(self):
        return self._age

    @property
    def dietary_needs(self):
        return self._dietary_needs

    @property
    def health_records(self):
        return self._health_records.copy()

    @property
    def environmental_type(self):
        return self._environmental_type

    @property
    def at_vet(self):
        return self._at_vet

    # Methods for subclasses
    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def get_category(self):
        pass

    # General methods
    def eat(self):
        self._last_fed = datetime.now()
        return f'{self._name} the {self._species} is sticking to their diet and eating {self._dietary_needs}.'

    def sleep(self):
        return f'{self._name} the {self._species} is sleeping.'

    def add_health_record(self, description: str, severity: str, treatment: str = ''):
        if severity not in ['low', 'medium', 'high']:
            raise ValueError('Severity must be one of "low", "medium", "high".')
        self._health_records.append({
            'description': description,
            'date': datetime.now(),
            'severity': severity,
            'treatment': treatment
        })

    def __str__(self):
        return f'{self._name} the {self._species} is {self._age} years old.'






