# Ask the user for a number and determine whether the number is prime or not.

def check_primality(range_numb, numb):
    range_numb = [y for y in range_numb if numb % y == 0]
    if range_numb:
        return range_numb
    else:
        return "Empty. No divisors."


number = int(input("Give me a number: "))
# empty list for range
d = []

for x in range(2, number):
    d.append(x)

print("Divisors: ", check_primality(d, number))
