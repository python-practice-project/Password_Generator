# Password Generator
import random
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z''a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbol = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_']
print("Welcomr to the PyPassword Generator!")
alphabet_num = int(input("How many letters would you like in your password?\n"))
number_num = int(input("How many numbers would you like in your password?\n"))
symbol_num = int(input("How many symbols would you like in your password?\n"))
password_list = []
for letter in range(1, alphabet_num+1):
    letter = random.choice(alphabet)
    password_list.append(letter)
for num in range(1, number_num+1):
    num = random.choice(number)
    password_list.append(num)
for sym in range(1, symbol_num+1):
    sym = random.choice(symbol)
    password_list.append(sym)
print(password_list)
random.shuffle(password_list)
print(password_list)
password = ''
for char in password_list:
    password += char
print(password)


