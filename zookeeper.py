from staff import Staff

class Zookeeper(Staff):
    def __init__(self, staff_id, name):
        super().__init__(staff_id, name, 'Zookeeper')

    def feed_animal(self, animal):
        animal_eat = animal.eat()
        return f'Zookeeper {self._name} - {animal_eat}'

    def clean_enclosure(self, enclosure):
        clean_enc = enclosure.clean()
        return f'Zookeeper {self._name} - {clean_enc}'

    def work(self):
        tasks = []
        tasks.append(f'{self._name} clocking in for work!')

        for animal in self._assigned_animals:
            tasks.append(self.feed_animal(animal))

        for enclosure in self._assigned_enclosures:
            tasks.append(self.clean_enclosure(enclosure))

        return '\n'.join(tasks)
