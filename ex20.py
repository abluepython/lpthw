#!/usr/bin/python3

from sys import argv # import from sys module the argv method

script, input_file = argv # unpack 2 variables for argv

def print_all(f): # define a function to use the .read() method from open function
    print(f.read())

def rewind(f): # define a function to use the .seek() method from open function wich will set's the file current position at the offset.
    f.seek(0)

def print_a_line(line_count, f): 
    print(line_count, f.readline())

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
