#fizzBuzz program to print fizz for multiples of 3 and buzz for multiples of 5 and fizzBuzz for multiples of both

#iterate from 1 to 50
for number in range(1,51):
    if number % 3 == 0 and number % 5 != 0:
        print("Fizz")
    elif number % 5 == 0 and number % 3 != 0:
        print("Buzz")
    elif number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    else:
        print(number)