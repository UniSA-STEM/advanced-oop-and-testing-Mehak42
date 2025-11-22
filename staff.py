'''
File: staff.py
Description: This class represents staff members of the zoo such has Zookeeper or Veterinarian.
Author: Mehakdeep Kaur Tiwana
ID: 110397073
Username: tiwmy001
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal, HealthIssue
from enclosure import Enclosure

class Staff:
    def __init__(self, name, role):
        self.__name = name
        self.__role = role
        self.__assigned_animals = []
        self.__assigned_enclosures = []

    def get_name(self):
        return self.__name
    def get_role(self):
        return self.__role
    def get_assigned_animals(self):
        return self.__assigned_animals
    def get_assigned_enclosures(self):
        return self.__assigned_enclosures

    def assign_animal(self, animal):
        if isinstance(animal, Animal):
            self.__assigned_animals.append(animal)
            print(f"{self.__name} has been assigned to {animal.name}")
        else:
            print("No animal assigned")








