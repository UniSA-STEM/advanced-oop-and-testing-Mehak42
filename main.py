'''
File: main.py
Description: This is the main class where i will be testing all 3 classes together
Author: Mehakdeep kaur Tiwana
ID: 110397073
Username: tiwmy001
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal, Mammal, Reptile, Bird, HealthIssue
from enclosure import Enclosure
from staff import Staff, Zookeeper, Veterinarian

print("\n========== ZOO SYSTEM DEMONSTRATION ==========\n")

"""TESTING ANIMAL CREATION & SUBCLASSES"""

print("\n--- Testing Animal Creation ---")
simba = Mammal("Simba", "Lion", 5, "Meat", "Healthy", "Golden Fur")
snake = Reptile("Jafar", "Snake", 2, "Mice", "Healthy", "Smooth Scales")
parrot = Bird("Pumpkin", "Parrot", 1, "Seeds", "Healthy", True)

print(simba)
simba.make_sound()
simba.eat()
simba.sleep()

print(snake)
snake.make_sound()
snake.shed_skin()

print(parrot)
parrot.make_sound()
parrot.fly()


""" 2. TESTING HEALTH ISSUES"""

print("\n--- Testing Health Issues ---")
issue1 = HealthIssue("Leg Injury", "2025-11-20", "High", "Bandaged and resting")
simba.add_health_issue(issue1)
simba.generate_list_of_health_issues()


""" 3. TESTING ENCLOSURE """

print("\n--- Testing Enclosure ---")
savannah = Enclosure("Savannah Habitat", 2, "Savannah")
print(savannah)

print("\n--- Adding Animals to Enclosure ---")
savannah.add_animal(simba)       # Allowed
savannah.add_animal(snake)     # Blocked (different species)
mufasa = Mammal("Mufasa", "Lion", 4, "Meat", "Healthy", "Light Fur")
savannah.add_animal(mufasa)      # Allowed

savannah.list_animals()

print("\n--- Removing Animals ---")
savannah.remove_animal(simba)
savannah.list_animals()

print("\n--- Cleaning Enclosure ---")
savannah.clean_enclosures()
print(savannah)

""" 4. TESTING STAFF """

print("\n--- Testing Staff ---")

""" Create staff """
zoo_keeper = Zookeeper("Kristin")
vet = Veterinarian("Dr. Jack")

print(zoo_keeper)
print(vet)

""" Assign responsibilities """
zoo_keeper.assign_enclosure(savannah)
zoo_keeper.assign_animal(mufasa)
zoo_keeper.assign_animal(snake)
vet.assign_animal(mufasa)

""" Staff performing duties """
print("\n--- Staff Performing Duties ---")
zoo_keeper.do_duties()
vet.do_duties()

""" Feeding + cleaning """
print("\n--- Zookeeper Actions ---")
zoo_keeper.feed_animal(mufasa)
zoo_keeper.feed_animal(snake)
zoo_keeper.clean_enclosure(savannah)

""" Veterinary actions """
print("\n--- Vet Actions ---")
vet.conduct_health_checks(mufasa)
vet.treat_animal(mufasa)
mufasa.generate_list_of_health_issues()


print("\n========== END ==========\n")