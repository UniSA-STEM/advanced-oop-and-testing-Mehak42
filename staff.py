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
        self.name = name
        self.role = role
        self.__assigned_animals = []
        self.__assigned_enclosures = []



