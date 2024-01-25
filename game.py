from art import logo
from art import vs
from game_data import data
import random

print(logo)


game_end = False

user_choice = ""

# function for random choice
def people_data(profile):
    print("name: ", profile.get("name", "N/A"))
    print("description: ", profile.get("description", "N/A"))
    print("country: ", profile.get("country", "N/A"))
  

random_people = random.sample(data, 2) 

for person in random_people:
    people_data(person)   
    print(vs)

user_choice = input("Enter your choice: ")    
def compare_answer():
    if user_choice["name:"]

#function for comparison