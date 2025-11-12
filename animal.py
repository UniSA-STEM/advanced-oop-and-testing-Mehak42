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

    name = property(get_name, set_name)
    species = property(get_species, set_species)
    age = property(get_age, set_age)
    dietary_needs = property(get_dietary_needs, set_dietary_needs)
    animal_health_status = property(get_animal_health_status,set_animal_health_status)

    def make_sound(self):
        print(f"{self.__name} the {self.__species} makes a sound")

    def eat(self):
        print(f"{self.__name} is eating {self.__dietary_needs} food.")

    def sleep(self):
        print(f"{self.__name} is sleeping at the moment.")

    def __str__(self):
        return (f"{self.__name} is {self.__species} and is {self.__age} years old. Dietary needs: {self.__dietary_needs}."
                f"Health status: {self.__animal_health_status}.")

class Mammal(Animal):
    def __init__(self, name, species, age, dietary_needs, animal_health_status, have_fur_type):
        super().__init__(name, species, age, dietary_needs, animal_health_status)
        self.__have_fur_type = have_fur_type

    def make_sound(self):
        print(f"{self.__name} the {self.__species} whines gently.")

    def feed_milk(self):
        print(f"{self.__name} feed the milk to their young ones.")

    def __str__(self):
        return super().__str__() + f"Fur type: {self.__have_fur_type}"

class Reptile(Animal):
    def __init__(self, name, species, age, dietary_needs, animal_health_status, scale_type):
        super().__init__(name, species, age, dietary_needs, animal_health_status)
        self.__scale_type = scale_type

    def make_sound(self):
        print(f"{self.__name} makes hiss sound.")

    def shed_skin(self):
        print(f"{self.__name} is shedding its {self.__scale_type} scale.")

    def __str__(self):
        return super().__str__() + f" Has {self.__scale_type} scales."






