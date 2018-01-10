from random import randint

ran_numb = randint(1, 9)

guess = int(input("Guess a number from 1 to 9: "))


def guess_numb(number1, number2):
    if number1 == number2:
        return "\n\n***Excellent! First chance and you won!***\n\n"
    else:
        while number1 != number2:
            if number1 > number2:
                print("\nThe number is too low")
                number2 = int(input("\nTry again... "))
            else:
                print("\nThe number is too high")
                number2 = int(input("\nTry again... "))
        else:
            return "\n\n*That's right*\n\n"


print(guess_numb(ran_numb, guess))