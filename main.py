'''
File: main.py
Description: A brief description of this Python module.
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

lion = Mammal('Beefcake', 'Lion', 3, 'Carnivore', 'Jungle')
eagle = Bird('Drilla', 'Wedge-Tailed Eagle', 2, 'Carnivore', 'Tropical')
snake = Reptile('Princely', 'Tiger Snake', 7, 'Carnivore', 'Jungle')

# Enclosure management
jungle_encl = Enclosure('Jungle Zone', 1500, 'Jungle', 60)
jungle_encl.add_animal(lion)
jungle_encl.add_animal(snake)
print(f'Enclosure: {jungle_encl}')

# Staff interactions
zk = Zookeeper('ZK01', 'Chancy')
vet = Veterinarian('VET01', 'Dr. Frodo')
zk.feed_animal(lion)
vet.health_check(lion)
print(zk.work())