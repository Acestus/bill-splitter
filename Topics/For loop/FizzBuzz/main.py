for i in range(1, 101):
    if i % 3 == 0 and i % 5 != 0:
        print("Fizz")
    elif i % 5 == 0 and i % 3 != 0:
        print("Buzz")
    elif i % 15 == 0 and i != 0:
        print("FizzBuzz")
    else:
        print(i)