# collect user imput
# - length of password
# - should include uppercase
# - should include special 
# - should include digits 

# get all available charachters based on user prefrence 
# randomly pick charachter as per lentghj
# it at least have one charachter for all user prefrences 
# ensure legth is valid for choosen user prefrences

import random  
import string  # give access to all string, upper/lowercase, digits, specials.

def genrate_password():
    length = int(input("Enter a deired legth for the password : ").strip())
    include_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower()
    include_special = input("Include special characters? (yes/no): ").strip().lower()
    include_digits = input("Include digits? (yes/no): ").strip().lower()

    if length < 4 :
        print("Password length must be at least 4 characters.")
        return
    
    lower = string.ascii_lowercase  # gives --> 'abcdefghijklmnopqrstuvwxyz'
    upper = string.ascii_uppercase if include_uppercase == 'yes' else '' # gives --> 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    specia = string.punctuation if include_special == 'yes' else '' # gives --> '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    digit = string.digits if include_digits == 'yes' else  ''  # gives --> '0123456789'

    avilable_characters = lower + upper + specia + digit
    # print(f"Available characters: {avilable_characters}")  # Debugging line to see available characters

    required_characters = []
    if include_uppercase == 'yes':
        required_characters.append(random.choice(upper))
    if include_special == 'yes':
        required_characters.append(random.choice(specia))
    if include_digits == 'yes':
        required_characters.append(random.choice(digit))

    # print(required_characters)

    remaining_length = length - len(required_characters)
    remaining_characters = random.choices(avilable_characters, k=remaining_length) # choose remaining characters randomly from available characters
    # print(remaining_characters)


    # other way to do that ⬆️ is 
    # for _ in range(remaining_length):
    #     character = random.choice(avilable_characters)
    #     remaining_characters.append(character)


    password = required_characters + remaining_characters # its an array now
    print(password)
    random.shuffle(password)  # shuffle the password to make it random
    # print(password)  # Debugging line to see the password list

    # convert into string with joimg with "" this ie no gap btw two consicative characters/elements normally use to seprate elements with " " or |

    password = ''.join(password)  # join the list into a string with no space
    print(f"Generated Password: {password}")  # print the final password


genrate_password()