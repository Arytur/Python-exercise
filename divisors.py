# Create a program that asks the user for a number
# and then prints out a list of all the divisors of that number.

numb = int(input("Please tell me a number:"))

x = range(2, numb + 1)
lista = []
for n in x:
    if numb % n == 0:
        lista.append(n)

print("Divisors:", lista)
