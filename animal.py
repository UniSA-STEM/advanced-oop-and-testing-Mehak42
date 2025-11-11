'''
File: animal.py
Description: Defines animal class used in the zoo management system.
Author: Mehakdeep Kaur Tiwana
ID: 110397073
Username: tiwmy001
This is my own work as defined by the University's Academic Integrity Policy.
'''

class Animal:
    def __init__(self, name, species, age, dietary_needs, animal_health_status):
        self.__name = name
        self.__species = species
        self.__age = age
        self.__dietary_needs = dietary_needs
        self.__animal_health_status = animal_health_status

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
    def set_animal_health_status(self, animal_health_status, status):
        self.__animal_health_status = status



