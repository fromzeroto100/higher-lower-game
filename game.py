from art import logo
from art import vs
from game_data import data
import random
# Display art
print(logo)


game_end = False

user_choice = ""


# def people_data(profile):
#     print("name: ", profile.get("name", "N/A"))
#     print("description: ", profile.get("description", "N/A"))
#     print("country: ", profile.get("country", "N/A"))
  

# random_people = random.sample(data, 2) 
 

# for person in random_people:
#     people_data(person)   
#     print(vs)

# user_choice = input("Enter your choice: ")    
def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"
# Generate a random account from the game
account_a = random.choice(data)
account_b = random.choice(data)

if account_a == account_b:
    account_b = random.choice(data)
print(f"Compare A: {format_data(account_a)}") 
print(vs)   
print(f"Compare B: {format_data(account_b)}") 
  
# Format the account data into printable format

# Ask user for a guess

# Check if user is correct.

# Get follower count of each account

# Use if statement to check if user is correct

# Give user feedback on their guess 

# Score keeping

# Making account at position B become next account at position A

# Clear the screen between rounds