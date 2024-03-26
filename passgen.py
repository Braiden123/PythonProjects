from random import *

def passgen(length):
    import string
    import random
    ranchar = string.ascii_letters
    password = ''
    for letter in range(length - 2):
        #Randomly choose letters except for the last two characters
        password += random.choice(string.ascii_letters)
    for number in range(2):
        #Add two random digits to the end of the string
        randnum = randint(0, 9)
        password += str(randnum)
    return password

while True:
    print("Please enter the integer length of the password you wish to generate.")
    print("Must be between 8-20 inclusive, otherwise press 0 to exit.")
    userlen = input("Length = ")
    try:
        userlen = int(userlen)
    except ValueError:
        print("This is not an integer")
    if userlen == 0:
        break
    elif (userlen < 8) or (userlen > 20):
        print("Please enter an integer between 8 to 20, inclusive.")
    else:
        print("Generating password...")
        newpass = passgen(userlen)
        print("Your password is: " + newpass)
