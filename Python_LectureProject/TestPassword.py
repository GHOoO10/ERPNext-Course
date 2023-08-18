import string
'''
string.ascii_letters
The concatenation of the ascii_lowercase and ascii_uppercase constants described below.
 This value is not locale-dependent.

string.ascii_lowercase
The lowercase letters 'abcdefghijklmnopqrstuvwxyz'. This value is not locale-dependent and will not change.

string.ascii_uppercase
The uppercase letters 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'. This value is not locale-dependent and will not change.

string.digits
The string '0123456789'.

string.punctuation
String of ASCII characters which are considered punctuation characters in the C locale:
 !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~.
'''
def test_password(password):
    # Define the criteria for a valid password
    min_length = 8
    requires_lowercase = True
    requires_uppercase = True
    requires_digit = True
    requires_special = True
    special_chars = string.punctuation 
    # string.punctuation = String of ASCII characters which are considered punctuation characters in the C locale: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    

    # Check the length of the password
    if len(password) < min_length:
        return "weak"

    # Check if lowercase letters are required
    if requires_lowercase and not any(char.islower() for char in password):
        return "weak"

    # Check if uppercase letters are required
    if requires_uppercase and not any(char.isupper() for char in password):
        return "weak"

    # Check if digits are required
    if requires_digit and not any(char.isdigit() for char in password):
        return "weak"

    # Check if special characters are required
    if requires_special and not any(char in special_chars for char in password):
        return "medium"

    # All tests passed, the password is strong
    return "strong"

# Prompt the user to enter a password
password = input("Enter a password: ")

# Test the password
password_strength = test_password(password)

# Provide feedback to the user based on password strength
if password_strength == "weak":
    print("Weak password. Please choose a stronger password. More than 8 char.")
elif password_strength == "medium":
    print("Medium password. Consider adding more complexity to strengthen it.")
else:
    print("Strong password! Good job!")