number = int(input("please enter your number : "))
if number% 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 5 == 0:
    print("BUZZ")
elif number % 3 == 0:
    print("Fizz")
else:
    print("number not allowed dived to 3 or 5 ")