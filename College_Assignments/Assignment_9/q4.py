import random

class SmallNumberError(Exception): pass

number = random.random()
print(f"Generated Number: {number}")

if number < 0.1:
    raise SmallNumberError("Number is below 0.1")
