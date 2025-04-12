import math
import random

# Define a tuple of East African cities with their coordinates (latitude, longitude)
cities = (
    ("Kampala", (0.3476, 32.5825)),
    ("Nairobi", (-1.2864, 36.8172)),
    ("Dar es Salaam", (-6.7924, 39.2083)),
    ("Addis Ababa", (9.1450, 38.7131)),
    ("Kigali", (-1.9706, 30.1044)),
)

# Function to calculate the distance between two sets of coordinates using the Haversine formula
def haversine_distance(coord1, coord2):
    R = 6371.0  # Radius of Earth in kilometers
    lat1, lon1 = math.radians(coord1[0]), math.radians(coord1[1])
    lat2, lon2 = math.radians(coord2[0]), math.radians(coord2[1])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c  # Distance in kilometers
    return distance

# Game instructions and initialization
print("Welcome to the East Africa City Distance Guessing Game!")
print("Your task is to guess which city is closest to a given city.")
print("You have 3 attempts to guess correctly.")
print("Available cities: ", ", ".join(city for city, _ in cities))

# Select a random city as the target city
target_city, target_coordinates = random.choice(cities)

# Start the game
attempts = 3
while attempts > 0:
    print(f"\nGuess which city is closest to {target_city}.")
    # Show the available options (excluding the target city itself)
    print("Options: ", ", ".join(city for city, _ in cities if city != target_city))
    
    # Get the player's guess
    guess = input("Enter your guess: ").title()
    
    # Check if the guessed city exists
    guessed_coordinates = None
    for city, coordinates in cities:
        if city == guess:
            guessed_coordinates = coordinates
            break
    
    # If the guess is valid
    if guessed_coordinates:
        # Calculate the distance between the guessed city and the target city
        distance = haversine_distance(target_coordinates, guessed_coordinates)
        print(f"The distance between {target_city} and {guess} is {distance:.2f} kilometers.")
        
        # Find the closest city (excluding the target city itself)
        closest_city = min(
            (city for city in cities if city[0] != target_city),  # Exclude target city
            key=lambda city: haversine_distance(target_coordinates, city[1])
        )
        
        if guess == closest_city[0]:
            print(f"Congratulations! {guess} is the closest city to {target_city}. You win!")
            break
        else:
            print(f"Sorry, {guess} is not the closest city.")
            attempts -= 1
            print(f"You have {attempts} attempts remaining.")
    else:
        print(f"{guess} is not a valid city. Try again.")

# If the player runs out of attempts
if attempts == 0:
    print(f"Game Over! The closest city to {target_city} was {closest_city[0]}.")