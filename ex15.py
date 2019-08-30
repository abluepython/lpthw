#!/usr/bin/python3
from sys import argv # imports from sys modules the argv method 

script, filename = argv # give to argv two arguments

txt = open(filename) # open the filename using the open method

print(f"Here's your file {filename}: ") # print the filename on the screen
print(txt.read()) # print what is inside the filename
txt.close()

print("Type the filename again: ") # print to the user to type in again the filename or another filename
file_again = input("> ") # prompt a message to the screen and save the user input to a variable

txt_again = open(file_again) # open the file again with the open method

print(txt_again.read()) # print what is inside the filename
txt_again.close()
