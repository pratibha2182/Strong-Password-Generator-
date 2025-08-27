import random  
import string

def generate_strong_password(length=12):
    if length < 4:
        return "Password length should be at least 4"

    # Characters sets
    letters_lower = string.ascii_lowercase
    letters_upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Ensure at least one character from each category
    password = [
        random.choice(letters_lower),
        random.choice(letters_upper),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest of the password length
    all_chars = letters_lower + letters_upper + digits + symbols
    password += [random.choice(all_chars) for _ in range(length - 4)]

    # Shuffle to randomize the order
    random.shuffle(password)

    # Convert list to string
    return ''.join(password)

# Main program
if __name__ == "__main__":
    length = int(input("Enter desired password length: "))
    print("Strong Password:", generate_strong_password(length))