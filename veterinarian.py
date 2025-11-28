from staff import Staff
from healthRecord import HealthRecord

class Veterinarian(Staff):
    def __init__(self, staff_id, name):
        super().__init__(staff_id, name, 'Veterinarian')

    def health_check(self, animal):
        unresolved_problems = [issue for issue in animal.health_records if not issue.resolved]

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
        if health_record in animal.health_records:
            health_record.is_healed()
            return f'Veterinarian: {self._name} - Treated {animal.name} for {health_record.description}.'
        return f'No health record for {animal.name}'

    def work(self):
        tasks = []
        tasks.append(f'{self._name} clocking in for work!')

        for animal in self._assigned_animals:
            tasks.append(self.health_check(animal))
        return '\n'.join(tasks)

