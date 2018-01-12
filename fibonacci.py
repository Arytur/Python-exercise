def fibonacci(numbers):
    fibonacci_list = list()
    a = 0
    b = 1
    c = 1
    for x in range(1, numbers + 1):
        fibonacci_list.append(c)
        c = a + b
        a = b
        b = c
    return fibonacci_list


number = int(input("How many numbers do you want to generate? "))
print("This is a fibonacci list: ")
print(fibonacci(number))
