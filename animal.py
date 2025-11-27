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
        self.__at_vet = False

    # Properties for getters
    @property
    def name(self):
        return self.__name

    @property
    def species(self):
        return self.__species

    @property
    def age(self):
        return self.__age

    @property
    def dietary_needs(self):
        return self.__dietary_needs

    @property
    def health_records(self):
        return self.__health_records

    @property
    def environmental_type(self):
        return self.__environmental_type

    # Methods for subclasses
    @abstractmethod
    def make_sound(self):
        pass

    # General methods
    def eat(self):
        return f'{self.__name} the {self.__species} is sticking to their diet and eating {self.__dietary_needs}.'

    def sleep(self):
        return f'{self.__name} the {self.__species} is sleeping.'

    def add_health_record(self, description: str, severity: str, treatment: str = ''):
        if severity not in ['low', 'medium', 'high']:
            raise ValueError('Severity must be one of "low", "medium", "high".')
        self.__health_records.append({
            'description': description,
            'date': datetime.now(),
            'severity': severity,
            'treatment': treatment
        })

    def get_health_report(self):
        if not self.__health_records:
            return f'{self.__name} is healthy.'
        report = f'Health Report: {self.__name}\n'
        for record in self.__health_records:
            report += f' - {record['description']} ({record['severity']}) {record["treatment"]}\n'
        return report

    def add_to_enclosure(self, enclosure):
        if not isinstance()







