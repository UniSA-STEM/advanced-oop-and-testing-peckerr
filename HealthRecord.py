from datetime import datetime

class HealthRecord:

    SEVERITIES = ['low', 'medium', 'high']

    def __init__(self, description, severity, date_reported=None, treatment_plan=None, notes=None):
        if not isinstance(description, str):
            raise ValueError('Description must be a string')
        if severity not in self.SEVERITIES:
            raise ValueError (f'Severity must be one of {self.SEVERITIES}')

        self._description = description
        self._severity = severity
        self._date_reported = date_reported if date_reported else datetime.now()
        self._treatment_plan = treatment_plan if treatment_plan else 'No plan currently.'
        self._notes = notes if notes else ''
        self._resolved = False
        self._healed_date = None

    @property
    def description(self):
        return self._description

    @property
    def severity(self):
        return self._severity

    @property
    def date_reported(self):
        return self._date_reported

    @property
    def treatment_plan(self):
        return self._treatment_plan

    @property
    def notes(self):
        return self._notes

    @property
    def resolved(self):
        return self._resolved

    def update_treatment_plan(self, new_plan):
        if not isinstance(new_plan, str):
            raise ValueError('new_plan must be a string')
        self._treatment_plan = new_plan

    def add_notes(self, new_notes):
        if not isinstance(new_notes, str):
            raise ValueError('new_notes must be a string')
        self._notes += f'\n{new_notes}'

    def is_healed(self):
        self._resolved = True
        self._healed_date = datetime.now()

    def __str__(self):
        status = 'Resolved' if self._resolved else 'Ongoing'
        return  (f'[{status}] {self._severity} - {self._description}'
                 f'Reported: {self._date_reported}')
