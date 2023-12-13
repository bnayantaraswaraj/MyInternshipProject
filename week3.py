import secrets
import string

def generate_password(length=12):
    # Define character sets for the password
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character sets
    all_characters = uppercase_letters + lowercase_letters + digits + special_characters

    # Ensure the password has a mix of characters
    password = secrets.choice(uppercase_letters)
    password += secrets.choice(lowercase_letters)
    password += secrets.choice(digits)
    password += secrets.choice(special_characters)

    # Fill the rest of the password with random characters
    for _ in range(length - 4):
        password += secrets.choice(all_characters)

    # Shuffle the password to mix the characters
    password_list = list(password)
    secrets.SystemRandom().shuffle(password_list)
    password = ''.join(password_list)

    return password

if __name__ == "__main__":
    password_length = int(input("Enter the desired password length: "))
    password = generate_password(password_length)

    print("Generated Password:", password)
