player1 = input("\nPlayer one name:")
player2 = input("\nPlayer two name:")

x = """\nChoose Rock, Paper or Scissors
  1 = Rock
  2 = Paper
  3 = Scissors\n"""
print(x)


choose1 = int(input("\nWhat you choose to play, %s:" % player1))

while choose1 > 3:
    print("\nWrong value!\n", x)
    choose1 = int(input("\nWhat you choose to play, %s:" % player1))

choose2 = int(input("\nWhat you choose to play, %s:" % player2))

while choose2 > 3:
    print("\nWrong value!\n", x)
    choose2 = int(input("\nWhat you choose to play, %s:" % player2))


while choose1 == choose2:
    print("\nIt's a tie. Please choose something else, both of you\n")
    choose1 = int(input("\nWhat you choose to play, %s:" % player1))
    while choose1 > 3:
        print("\nWrong value!\n", x)
        choose1 = int(input("\nWhat you choose to play, %s:" % player1))
    choose2 = int(input("\nWhat you choose to play, %s:" % player2))
    while choose2 > 3:
        print("\nWrong value!\n", x)
        choose2 = int(input("\nWhat you choose to play, %s:" % player2))


b = ["It's", "time", "to", "begin", "our", "tournament!"]
print('\n\n')
for x in b:
    print('***', x, '***')


if choose1 == 1 and choose2 == 2:
    print("\n\n******Player %s win!******\n\n" % player2)
elif choose1 == 1 and choose2 == 3:
    print("\n\n******Player %s win!******\n\n" % player1)
elif choose1 == 2 and choose2 == 1:
    print("\n\n******Player %s win!******\n\n" % player1)
elif choose1 == 2 and choose2 == 3:
    print("\n\n******Player %s win!******\n\n" % player2)
elif choose1 == 3 and choose2 == 1:
    print("\n\n******Player %s win!******\n\n" % player2)
elif choose1 == 3 and choose2 == 2:
    print("\n\n******Player %s win!******\n\n" % player1)


