#!/usr/bin/python3

def create_list(increment, num):
    """Type in how many numbers you want to add to the list"""
    numbers = []
    i = 0
    while i < num:
        print(f"At the top i is {i}")
        numbers.append(i)
        i += increment

        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

def create_list2(increment, num):
    numbers = []
    for i in range(0, num, increment):
        print(f"At the top i is {i}")
        numbers.append(i)
        print("Numbers now: ", numbers)

numbers = create_list2(2, 15)

print(numbers)
