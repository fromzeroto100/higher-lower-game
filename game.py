from art import logo
from art import vs
from game_data import data
import random
# Display art
print(logo)



# def people_data(profile):
#     print("name: ", profile.get("name", "N/A"))
#     print("description: ", profile.get("description", "N/A"))
#     print("country: ", profile.get("country", "N/A"))
  

# random_people = random.sample(data, 2) 
 

# for person in random_people:
#     people_data(person)   
#     print(vs)

# Generate a random account from the game
def get_random_account():
    return random.choice(data)

# Format the account data into printable format
def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]

    return(f"{name}: a {description}, from {country}")
# Ask user for a guess

# Check if user is correct.

# Get follower count of each account

# Use if statement to check if user is correct

# Give user feedback on their guess 

# Score keeping

# Making account at position B become next account at position A

# Clear the screen between rounds