from random import randint

ran_numb = randint(1, 9)

guess = int(input("\nGuess a number from 1 to 9: "))


def guess_numb(number1, number2):
    if number1 == number2:
        return "\n\n***Excellent! First chance and you won!***\n\n"
    else:
        count = 1
        print("\nSorry, wrong number.\n\nDo you want to continue? y or n")
        yesno = input('')
        if yesno != 'n':
            while number1 != number2:
                count += 1
                if number1 > number2:
                    print("\nThe number %d is too low." % number2)
                    number2 = int(input("\nTry again... "))
                else:
                    print("\nThe number %d is too high." % number2)
                    number2 = int(input("\nTry again... "))
            else:
                return "\n\n*That's right. It's a number %d.*\n\n You needed %d tries to guess this number.\n" % (number1, count)
        elif yesno == 'n':
            return "Exit the game."


print(guess_numb(ran_numb, guess))