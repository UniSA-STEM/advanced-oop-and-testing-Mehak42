'''
File: filename.py
Description: This is the main class where i will be testing all 3 classes together
Author: Mehakdeep kaur Tiwana
ID: 110397073
Username: tiwmy001
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal, Mammal, Reptile, Bird, HealthIssue
from enclosure import Enclosure

print("\n--- Testing Animal Creation ---")
leo = Mammal("Leo", "Lion", 5, "Meat", "Healthy", "Golden Fur")
print(leo)
leo.make_sound()
leo.eat()
leo.sleep()

print("\n--- Adding Health issue to an animal ---")
injury = HealthIssue("Leg Injury", "2024-11-20", "High", "Bandaged and resting")
leo.add_health_issue(injury)
leo.generate_list_of_health_issues()