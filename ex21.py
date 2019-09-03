#!/usr/bin/python3

def add(a, b):
    print(f"Adding {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"Subtracting {a} - {b}")
    return a - b

def multiply(a, b):
    print("Multiplying {a} * {b}")
    return a * b

def devide(a, b):
    print("Dividing {a} / {b}")
    return a / b

print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = devide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# A puzzle for extra credit, type it in anyway.
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, devide(iq, 2))))
formula = 35 + (74 - (180 * (50 / 2)))


print("That becomes: ", what, " Can you do it by Hand?")

