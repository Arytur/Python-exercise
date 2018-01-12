def fibonacci(numbers):
    fibonacci_list = [1]
    a = 0
    b = 1
    for x in range(1, numbers + 1):
        c = a + b
        a = b
        b = c
        fibonacci_list.append(c)
    return fibonacci_list


number = int(input("How many numbers do you want to generate? "))
print("This is a fibonacci list: ")
print(fibonacci(number))
