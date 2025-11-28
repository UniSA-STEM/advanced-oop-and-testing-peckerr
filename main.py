'''
File: main.py
Description: Walkthrough of the zoo.
Author: Thomas Cochrane
ID: 110466784
Username: COCTY007
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal
from mammal import Mammal
from reptile import Reptile
from bird import Bird

from staff import Staff
from zookeeper import Zookeeper
from veterinarian import Veterinarian

from enclosure import Enclosure
from healthRecord import HealthRecord

print('=== Demo Start ===')

tiger = Mammal('Beefcake', 'tiger', 3, 'Carnivore', 'Jungle')
eagle = Bird('Drilla', 'Wedge-Tailed Eagle', 2, 'Carnivore', 'Tropical')
snake = Reptile('Princely', 'Tiger Snake', 7, 'Carnivore', 'Jungle')

print('Created animals:')
print(f'- {tiger}')
print(f'- {eagle}')
print(f'- {snake.make_sound()}\n')

# Enclosure management with environment/species validation
jungle_encl = Enclosure('Jungle Zone', 1500, 'Jungle', 60)
tropical_encl = Enclosure('Bird Sanctuary', 800, 'Tropical', 90)

jungle_encl.add_animal(tiger)
tropical_encl.add_animal(eagle)

print('Enclosures populated:')
print(f'Jungle: {jungle_encl} (Cleanliness: {jungle_encl.cleanliness_level}%)')
print(f'Tropical: {tropical_encl}\n')

# Staff creation and animal assignments
zk1 = Zookeeper('ZK001', 'Bob')
zk2 = Zookeeper('ZK002', 'Alice')
vet = Veterinarian('VET001', 'Dr. Jones')

# Assign animals to staff for work() method demonstration
zk1.assign_animal(tiger)
zk2.assign_animal(eagle)
zk2.assign_enclosure(tropical_encl)
vet.assign_animal(tiger)

# Health record demonstration
tiger.add_health_record('Sore paw', 'medium', 'Antibiotics')
print(f'{tiger.name} health records: {len(tiger.health_records)}\n')

# Execute daily operations
print('=== Daily Staff Operations ===')
print(zk1.work())
print('\n' + zk2.work())
print('\n' + vet.work())

# Veterinary treatment workflow
print('\n=== Medical Treatment Demo ===')
print(vet.treat_animal(tiger, tiger.health_records[0]))
print(f'Post-treatment check: {vet.health_check(tiger)}')

# Zookeeper maintenance
print(f'\nEnclosure cleaned: {zk2.clean_enclosure(tropical_encl)}')

print('\n=== Demo Complete ===')