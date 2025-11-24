'''
File: animal.py
Description: Defines animal class used in the zoo management system.
Author: Mehakdeep Kaur Tiwana
ID: 110397073
Username: tiwmy001
This is my own work as defined by the University's Academic Integrity Policy.
'''

class HealthIssue:
    """Represents a single health issue for an animal."""
    def __init__(self, description, date_reported, severity_level, treatment_notes = None):
        self.__description = description
        self.__date_reported = date_reported
        self.__severity_level = severity_level
        self.__treatment_notes = treatment_notes

    """getters and setters"""
    def get_description(self):
        return self.__description
    def get_date_reported(self):
        return self.__date_reported
    def get_severity_level(self):
        return self.__severity_level
    def get_treatment_notes(self):
        return self.__treatment_notes

    def set_treatment_notes(self, notes):
        self.__treatment_notes = notes

    def __str__(self):
        return (f"Health Issue: {self.__description}, Date: {self.__date_reported}, "
                f"Severity Level: {self.__severity_level}, Treatment Notes: {self.__treatment_notes}")

"""BASE CLASS ANIMAL (PARENT CLASS FOR MAMMAL, BIRD, REPLTILE"""
class Animal:
    def __init__(self, name, species, age, dietary_needs, animal_health_status):
        self.__name = name
        self.__species = species
        self.__age = age
        self.__dietary_needs = dietary_needs
        self.__animal_health_status = animal_health_status

        self.__health_issues = []

    def get_name(self):
        return self.__name
    def get_species(self):
        return self.__species
    def get_age(self):
        return self.__age
    def get_dietary_needs(self):
        return self.__dietary_needs
    def get_animal_health_status(self):
        return self.__animal_health_status
    def set_name(self, name):
        self.__name = name
    def set_species(self, species):
        self.__species = species
    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            print("Invalid age")
    def set_dietary_needs(self, dietary_needs):
        self.__dietary_needs = dietary_needs
    def set_animal_health_status(self, status):
        self.__animal_health_status = status

    name = property(get_name, set_name)
    species = property(get_species, set_species)
    age = property(get_age, set_age)
    dietary_needs = property(get_dietary_needs, set_dietary_needs)
    animal_health_status = property(get_animal_health_status,set_animal_health_status)

    """Methods for health management"""

    def add_health_issue(self, health_issue):
        """adds a health issue to the list of health issues."""
        if isinstance(health_issue, HealthIssue):
            self.__health_issues.append(health_issue)
            print(f"Added Health Issue for {self.get_name()}")
        else:
            print("Invalid Health Issue")

    def generate_list_of_health_issues(self):
        """generates a list of health issues."""
        print(f"Generating list of Health Issues for {self.get_name()}")
        if not self.__health_issues:
            print("No Health Issues generated.")
        for problems in self.__health_issues:
            print(problems)

    def make_sound(self):
        """general sound the animals make"""
        print(f"{self.get_name()} the {self.get_species()} makes a sound")

    def eat(self):
        print(f"{self.get_name()} is eating {self.get_dietary_needs()} food.")

    def sleep(self):
        print(f"{self.get_name()} is sleeping at the moment.")

    def __str__(self):
        return (f"{self.get_name()} is {self.get_species()} and is {self.get_age()} years old. Dietary needs: {self.get_dietary_needs()}."
                f"Health status: {self.get_animal_health_status()}.")

class Mammal(Animal):
    """SUBCLASS OF ANIMAL"""
    def __init__(self, name, species, age, dietary_needs, animal_health_status, have_fur_type):
        super().__init__(name, species, age, dietary_needs, animal_health_status)
        self.__have_fur_type = have_fur_type

    def make_sound(self):
        """Polymorphic method for making animal sound"""
        print(f"{self.get_name()} the {self.get_species()} whines gently.")

    def feed_milk(self):
        """unique behaviour of mammals"""
        print(f"{self.get_name()} feed the milk to their young ones.")

    def __str__(self):
        return super().__str__() + f" Fur type: {self.__have_fur_type}"

class Reptile(Animal):
    def __init__(self, name, species, age, dietary_needs, animal_health_status, scale_type):
        super().__init__(name, species, age, dietary_needs, animal_health_status)
        self.__scale_type = scale_type

    def make_sound(self):
        print(f"{self.get_name()} the {self.get_species()} makes hiss sound.")

    def shed_skin(self):
        print(f"{self.get_name()} is shedding its {self.__scale_type} scale.")

    def __str__(self):
        return super().__str__() + f" Has {self.__scale_type} scales."

class Bird(Animal):
    def __init__(self, name, species, age, dietary_needs, animal_health_status, can_fly):
        super().__init__(name, species, age, dietary_needs, animal_health_status)
        self.__can_fly = can_fly

    def make_sound(self):
        print(f"{self.get_name()} the {self.get_species()} chirps.")

    def fly(self):
        if self.__can_fly:
            print(f"{self.get_name()} is flying in the sky.")
        else:
            print(f"{self.get_name()} cannot fly.")

    def __str__(self):
        fly_or_not = "can fly" if self.__can_fly else "cannot fly"
        return super().__str__() + f" This bird {fly_or_not}."




