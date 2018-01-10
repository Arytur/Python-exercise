import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
d = random.sample(range(40), 9)
e = random.sample(range(55), 13)

c = list(set([x for x in a for y in b if x == y]))
print("a =", a)
print("b =", b)
print("\ncommon value in [a] and [b] =", c, "\n")

print("Random lists:\n")

f = list(set([a for a in d for b in e if a == b]))
print("d =", sorted(d))
print("e =", sorted(e))
print("\ncommon value in [d] and [e] =", sorted(f), "\n")