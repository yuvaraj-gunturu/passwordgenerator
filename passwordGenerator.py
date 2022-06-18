#Password genetaror
import random

chars ="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*(),.?1234567890"

number = int(input("Amount of passwords to generate:"))

length = int(input("your password length:"))

for pwd in range(number):
    password = ""
    for c in range(length):
        password += random.choice(chars)
    print(password)
        

