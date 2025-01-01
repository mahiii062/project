"""

Simple Python Project
Random PassWord Generator
8 Digits

"""

import random

def mixUp(string):
    rand_list = list(string)
    random.shuffle(rand_list)
    return ''.join(rand_list)

var1 = chr(random.randint(65, 90))   # Random uppercase letter (A-Z)
var2 = chr(random.randint(65, 90))
var3 = chr(random.randint(97, 122))  # Random lowercase letter (a-z)
var4 = chr(random.randint(97, 122))
var5 = chr(random.randint(48, 57))   # Random digit (0-9)
var6 = chr(random.randint(48, 57))
var7 = random.choice('!@#$%^&*()-_=+[]{}|;:,.<>?/')
var8 = random.choice('!@#$%^&*()-_=+[]{}|;:,.<>?/')

password = var1 + var2 + var3 + var4 + var5 + var6 + var7 + var8

password = mixUp(password)

print(password)
