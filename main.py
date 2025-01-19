# import libraries
import string
import random

# store all characters in list (uppercase, lowercase, digits, punctuation)
s1 = list (string.ascii_uppercase)
s2 = list (string.ascii_lowercase)
s3 = list (string.digits)
s4 = list (string.punctuation)

# shuffle all lists
random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

# take a number of characters from user and make sure the number is >= 6
chars_number = input("How many characters for the password?: (must be >=6)")

while True:
    try:
        chars_number = int (chars_number)
        if chars_number < 6 :
            print ("Password must be 6 characters at least")
            chars_number = input("How many characters for the password?: (must be >=6)")
        else:
            break
    
    except:
        print ("Pleae enter only numbers")
        chars_number = input("How many characters for the password?: (must be >=6)")

# create a password 60% of letters and 40% of digits and punctuations
part1 = round (chars_number * 0.3)
part2 = round (chars_number * 0.2)

password = []

for i in  range (part1):
    password.append(s1[i])
    password.append(s2[i])

for i in  range (part2):
    password.append(s3[i])
    password.append(s4[i])

password = "".join(password)
print (password)





        





