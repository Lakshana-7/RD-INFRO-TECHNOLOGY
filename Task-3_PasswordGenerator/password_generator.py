import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

try:
    user_input = int(input("Enter the desired password length: "))
    if user_input <= 0:
        print("Please enter a length greater than 0.")
    else:
        result = generate_password(user_input)
        print("Generated Password:", result)
except ValueError:
    print("Invalid input! Please enter a number.")