'''
File: staff.py
Description: A brief description of this Python module.
Author: Thomas Cochrane
ID: 110466784
Username: COCTY007
This is my own work as defined by the University's Academic Integrity Policy.
'''

class Staff(ABC):
    def __init__(self, staff_id, name, role):
        if not isinstance(staff_id, str):
            raise ValueError('Staff ID must be a string.')
        if not isinstance(name, str):
            raise ValueError('Staff name must be a string.')
        if not isinstance(role, str):
            raise ValueError('Staff role must be a string.')

        self._staff_id = staff_id
        self._name = name
        self._role = role
        self._assigned_animals = []
        self._assigned_enclosures = []

    @property
    def staff_id(self):
        return self._staff_id

    @property
    def name(self):
        return self._name

    @property
    def role(self):
        return self._role

    @property
    def assigned_animals(self):
        return self._assigned_animals.copy()

    @property
    def assigned_enclosures(self):
        return self._assigned_enclosures.copy()

    def assign_animal(self, animal):
        if animal not in self._assigned_animals:
            self._assigned_animals.append(animal)

    def assign_enclosure(self, enclosure):
        if enclosure not in self._assigned_enclosures:
            self._assigned_enclosures.append(enclosure)

    @abstractmethod
    def perform_role(self):
        pass

    def __str__(self):
        return f'{self._role} {self._name}, Employee ID: {self._staff_id}.'