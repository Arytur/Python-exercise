import random
import string


def generate_password():
    print("How strong you want a password?")
    print("1. Weak")
    print("2. Medium")
    print("3. Strong")
    print("4. Very Strong")
    strength_choice = int(input('\n'))
    password = list()
    if strength_choice == 1:
        strength = 5
        while strength > 0:
            weak = random.choice('xxxxy')
            if weak == 'x':
                weak_rand = random.choice(string.ascii_lowercase)
                password.append(weak_rand)
            elif weak == 'y':
                weak_rand = random.choice(string.digits)
                password.append(weak_rand)
            strength -= 1
    elif strength_choice == 2:
        strength = 8
        while strength > 0:
            medium = random.choice('xxxxyy')
            if medium == 'x':
                medium_rand = random.choice(string.ascii_letters)
                password.append(medium_rand)
            elif medium == 'y':
                medium_rand = random.choice(string.digits)
                password.append(medium_rand)
            elif medium == 'z':
                medium_rand = random.choice(string.punctuation)
                password.append(medium_rand)
            strength -= 1
    elif strength_choice == 3:
        strength = 12
        while strength > 0:
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
            strength -= 1
    elif strength_choice == 4:
        strength = 18
        while strength > 0:
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
            strength -= 1
    return ''.join(password)


print("\nYour password: ", generate_password())
