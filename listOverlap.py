import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#  create 2 random lists
e = random.sample(range(30), 8)
f = random.sample(range(30), 12)


def compare(tab1, tab2):
    c = []
    for x in tab1:
        for y in tab2:
            if x == y:
                c.append(y)
    return list(set(c))


print("First list:\n", a)
print("Second list:\n", b)
print("\nThe same numbers are:\n", compare(a, b))


print("\nFirst random list:\n", sorted(e))
print("Second random list:\n", sorted(f))

g = (compare(e, f))
print("\nThe same numbers are:\n", sorted(g))

