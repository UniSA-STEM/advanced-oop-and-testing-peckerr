from staff import Staff
from healthRecord import HealthRecord

'''
File: veterinarian.py
Description: Subclass of Staff, for vets.
Author: Thomas Cochrane
ID: 110466784
Username: COCTY007
This is my own work as defined by the University's Academic Integrity Policy.
'''

class Veterinarian(Staff):
    def __init__(self, staff_id, name):
        super().__init__(staff_id, name, 'Veterinarian')

    def health_check(self, animal):
        unresolved_problems = [issue for issue in animal.health_records if not issue.get('resolved', True)]

        if unresolved_problems:
            health_state = f'{animal.name} has unresolved health issues.'
        else:
            health_state = f'{animal.name} has no health issues.'

        return f'Veterinarian: {self._name} - Health check completed: {health_state}'

    def add_to_record(self, animal, description, severity, treatment_plan=None):
        health_record = HealthRecord(
            description=description,
            severity=severity,
            treatment_plan=treatment_plan
        )
        animal.add_health_record(health_record)

        return (f'Veterinarian: {self._name} - Created a new record for {animal.name}' +
                f'{description} ({severity})')

    def treat_animal(self, animal, health_record):
        if isinstance(health_record, int):
            index = health_record
            if 0 <= index < len(animal.health_records):
                animal.health_records[index]['resolved'] = True
                return f'Veterinarian: {self._name} - Treated {animal.name} for {animal.health_records[index]["description"]}.'

            for i, record in enumerate(animal.health_records):
                if record['description'] == health_record['description']:
                    animal.health_records[i]['resolved'] = True
                    return f'Veterinarian: {self._name} - Treated {animal.name} for {health_record["description"]}.'

        return f'No matching health record for {animal.name}'

    def work(self):
        tasks = []
        tasks.append(f'{self._name} clocking in for work!')

        for animal in self._assigned_animals:
            tasks.append(self.health_check(animal))
        return '\n'.join(tasks)

