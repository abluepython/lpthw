#!/usr/bin/python3

myname = 'Zed A. Shaw'
myage = 35 # not a lie
myheight = 74 # inches
myweight = 180 # lbs
myeyes = 'Blue'
myteeth = 'White'
myhair = 'Brown'
cm = myheight * 2.54
kg = myweight * 0.545

print(f"Transform {myheight} pounds to {kg} kgs.")
print(f"Transform {myweight} inches to {cm} cm.")
print(f"Let's talk about {myname}.")
print(f"He's {myheight} inches tall.")
print(f"He's {myweight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {myeyes} eyes and {myhair} hair.")
print(f"His teeth are usually {myteeth} depending on the coffe.")

# this line is tricky, try to get it exactly right
total = myage + myheight + myweight
print(f"If I add {myage}, {myheight} and {myweight} I get {total}.")
