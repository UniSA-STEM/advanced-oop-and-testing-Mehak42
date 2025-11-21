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
    cleanliness_level = property(get_cleanliness_level, set_cleanliness_level)
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
        if self.check_animal_compatibility(animal):
            self.__animals.append(animal)

            if self.__species_allowed is None:
                self.__species_allowed = animal.species

            print(f"{animal.name} has been added to the Enclosure {self.__name}")
        else:
            print(f"{animal.name} could not be added to the Enclosure {self.__name}")

    def remove_animal(self, animal):
        if animal in self.__animals:
            self.__animals.remove(animal)
            print(f"{animal.name} has been removed from the Enclosure {self.__name}")
        else:
            print(f"{animal.name} is not found the Enclosure {self.__name}")

    def clean_enclosures(self):
        self.__cleanliness_level = "Clean"
        print(f"Enclosure '{self.__name}' has been cleaned.")

    def list_animals(self):
        print(f"\nTotal number of Animals in {self.__name} Enclosure:")
        if len(self.__animals) == 0:
            print("There are no animals in the Enclosure {self.__name}")
        else:
            for x in self.__animals:
                print(f"{x.name} ({x.species}), Health: {x.animal_health_status}")

    def __str__(self):
        return (f"Enclosure: '{self.__name}' [{self.__environment_type}] "
                f"\nCleanliness level: {self.__cleanliness_level}"
                f"\nAnimals: {len(self.__animals)}"
                f"\nTotal Size: {self.__size}")




