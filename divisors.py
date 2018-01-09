numb = int(input("Please tell me a number:"))

x = range(2, numb + 1)
lista = []
for n in x:
    if numb % n == 0:
        lista.append(n)

print("Divisors:", lista)
