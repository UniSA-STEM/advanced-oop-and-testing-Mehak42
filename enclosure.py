'''
File: filename.py
Description: Defines Enclosure class used to house animals in the zoo.
Author: Mehakdeep Kaur Tiwana
ID: 110397073
Username: tiwmy001
This is my own work as defined by the University's Academic Integrity Policy.
'''

class Enclosure:
    def __init__(self, name, size, environment_type, cleanliness_level):
        self.__name = name
        self.__size = size
        self.__environment_type = environment_type
        self.__cleanliness_level = cleanliness_level
        self.__animals = []

    def get_name(self):
        return self.__name

