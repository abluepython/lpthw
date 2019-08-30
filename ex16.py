#!/usr/bin/python3
from sys import argv # import from sys module the argv method

script, filename = argv # add variables to unpack to the argv methos 

print(f"We're going to erase {filename}.") # print using f-string formatting 
print("If you don't want that, hit CTRL-C (^C).") # print another string to the screen
print("If you do want that, hit RETURN.")

input('?') # get input from the user to continue runing the script

print("Opening the file...") # print another string to the screen
target = open(filename, 'w') # open the filename with the write argument

print("Truncating the file. GoodBye!") # print another string to the screen

line1 = input("line 1: ") # get input from the user using the input method
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

#target.write(line1) # write to the file what is kept inside the variables line1
#target.write('\n')
#target.write(line2)
#target.write('\n')
#target.write(line3)
#target.write('\n')

target.write(f"{line1}\n{line2}\n{line3}\n")
print("And finally, we close it.")
target.close() # close the file before exiting the script



