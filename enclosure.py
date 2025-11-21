'''
File: filename.py
Description: Defines Enclosure class used to house animals in the zoo.
Author: Mehakdeep Kaur Tiwana
ID: 110397073
Username: tiwmy001
This is my own work as defined by the University's Academic Integrity Policy.
'''
from animal import Animal


class Enclosure:
    def __init__(self, name, size, environment_type, cleanliness_level="Clean"):
        self.__name = name
        self.__size = size
        self.__environment_type = environment_type
        self.__cleanliness_level = cleanliness_level
        self.__animals = []
        self.__species_allowed = None

    def get_name(self):
        return self.__name
    def get_size(self):
        return self.__size
    def get_environment_type(self):
        return self.__environment_type
    def get_cleanliness_level(self):
        return self.__cleanliness_level
    def get_animals(self):
        return self.__animals
    def set_cleanliness_level(self, level):
        if level > 0 or level <= 100:
            self.__cleanliness_level = level
        else:
            print("Invalid cleanliness_level")

    name = property(get_name)
    size = property(get_size)
    environment_type = property(get_environment_type)
    cleanliness_level = property(get_cleanliness_level, set_cleanliness_level())
    animals = property(get_animals)

    def check_animal_compatibility(self, animal):

        if not isinstance(animal, Animal):
            print("Only animals allowed")
            return False

        if len(self.__animals) >= self.__size:
            print(f"Enclosure '{self.__name}' is fully packed. ")
            return False

        if self.__species_allowed is None:
            return True

        if animal.species != self.__species_allowed:
            print(f"Incompatible species. The Enclosure {self.__name} only accepts {self.__species_allowed} species.")
            return False
        return True

    def add_animal(self, animal):



