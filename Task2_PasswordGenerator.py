import random
import string

def custom_password_generator(length):
    # Define characters to choose from for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password with the specified length
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        # Prompt the user for the desired password length
        password_length = int(input("Enter the desired length of the password: "))

        # Check if the length is valid
        if password_length <= 0:
            print("Please enter a valid password length.")
        else:
            # Generate and display the password
            password = custom_password_generator(password_length)
            print("Generated Password:", password)

    except ValueError:
        print("Invalid input. Please enter a valid number for the password length.")

if __name__ == "__main__":
    main()
