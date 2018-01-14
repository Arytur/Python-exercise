# Write a password generator in Python.

import random
import string


def generate_password():
    print("How strong you want a password?\n1. Weak\n2. Medium\n3. Strong\n4. Very Strong")
    strength_choice = int(input('\n'))
    password = list()
    if strength_choice == 1:
        length = 5
        while length > 0:
            weak = random.choice('xxxxy')
            if weak == 'x':
                weak_rand = random.choice(string.ascii_lowercase)
                password.append(weak_rand)
            elif weak == 'y':
                weak_rand = random.choice(string.digits)
                password.append(weak_rand)
            length -= 1
    elif strength_choice == 2:
        length = 8
        while length > 0:
            medium = random.choice('xxxxyy')
            if medium == 'x':
                medium_rand = random.choice(string.ascii_letters)
                password.append(medium_rand)
            elif medium == 'y':
                medium_rand = random.choice(string.digits)
                password.append(medium_rand)
            length -= 1
    elif strength_choice == 3:
        length = 12
        while length > 0:
            strong = random.choice('xxxxxyyyyzz')
            if strong == 'x':
                strong_rand = random.choice(string.ascii_letters)
                password.append(strong_rand)
            elif strong == 'y':
                strong_rand = random.choice(string.digits)
                password.append(strong_rand)
            elif strong == 'z':
                strong_rand = random.choice(string.punctuation)
                password.append(strong_rand)
            length -= 1
    elif strength_choice == 4:
        length = 18
        while length > 0:
            vstrong = random.choice('xxxxyyyyzzz')
            if vstrong == 'x':
                vstrong_rand = random.choice(string.ascii_letters)
                password.append(vstrong_rand)
            elif vstrong == 'y':
                vstrong_rand = random.choice(string.digits)
                password.append(vstrong_rand)
            elif vstrong == 'z':
                vstrong_rand = random.choice(string.punctuation)
                password.append(vstrong_rand)
            length -= 1
    return ''.join(password)


print("\nYour password: ", generate_password())
