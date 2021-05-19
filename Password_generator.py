import string
import random

# print(string.ascii_letters)
# print(string.digits)
# print(string.punctuation)

# for generating a strong password, we need all above 3 strings, so we concatenate all the 3
characters = string.ascii_letters + string.digits + string.punctuation
print(characters)

# password = "".join(random.choice(characters) for  x in range(4))
# This will generate a pwd with fixed length, if we want pwd to be very strong and not be recognized by anyone
password = "".join(random.choice(characters) for  x in range(random.randint(8,16)))
# This will have variable length pwd
print(password)

