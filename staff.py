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

        """staff has assigned animals and enclosures"""
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
        """assigns animal to staff member"""
        if isinstance(animal, Animal):
            self.__assigned_animals.append(animal)
            print(f"{self.get_name()} has been assigned to {animal.name}.")
        else:
            print("No animal assigned")

    def assign_enclosure(self, enclosure):
        """assigns enclosure to staff member"""
        if isinstance(enclosure, Enclosure):
            self.__assigned_enclosures.append(enclosure)
            print(f"{self.get_name()} has been assigned to {enclosure.name}.")
        else:
            print("No enclosure assigned")

    def do_duties(self):
        """general duties performed by staff"""
        print(f"{self.get_name()} performs staff duties.")

    def __str__(self):
        return f"Staff: {self.get_name()}, role: {self.get_role()}"


class Zookeeper(Staff):
    def __init__(self, name):
        super().__init__(name, "Zookeeper")

    def feed_animal(self, animal):
        """feeds the assigned animal"""
        if isinstance(animal, Animal):
            print(f"{self.get_name()} feeds {animal.name} which is {animal.species}.")
            animal.eat()
        else:
            print("Invalid animal")

    def clean_enclosure(self, enclosure):
        """cleans enclosure"""
        if isinstance(enclosure, Enclosure):
            enclosure.clean_enclosures()
            print(f"{self.get_name()} cleaned enclosure {enclosure.name}")
        else:
            print("Invalid enclosure")

    def do_duties(self):
        """overrides staff.do_duties()"""
        print(f"{self.get_name()} performs zookeeper duties which are feeding and cleaning.")

class Veterinarian(Staff):
    def __init__(self, name):
        super().__init__(name, "Veterinarian")

    def conduct_health_checks(self, animal):
        """do health checks on animals"""
        if isinstance(animal, Animal):
            print(f"{self.get_name()} conducts health checks for {animal.name}")
            animal.generate_list_of_health_issues()
        else:
            print("Invalid animal.")

    def treat_animal(self, animal):
        """treats animals and add it to health issues list"""
        if isinstance(animal, Animal):
            new_health_issue = HealthIssue("Treatment and ointments applied", "Today", "Low", "Needs resting")
            animal.add_health_issue(new_health_issue)
            print(f"{self.get_name()} treated {animal.name}.")
        else:
            print("Invalid animal")

    def do_duties(self):
        """overrides staff.do_duties()"""
        print(f"{self.get_name()} performs veterinarian duties which are checking and giving health treatments.")

















