#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

ran_letters = []
ran_numbers = []
ran_symbols = []


#This is going to be repeated three times for letters, symbols, numbers since we haven't done functions yet in this Python course
#letter case
for number in range(0, nr_letters):
  random_index = random.randint(0, len(letters)-1)
  ran_letters.append(letters[random_index])

#number case
for number in range(0, nr_numbers):
  random_index = random.randint(0, len(numbers)-1)
  ran_numbers.append(numbers[random_index])

#symbol case
for number in range(0, nr_symbols):
  random_index = random.randint(0, len(symbols)-1)
  ran_symbols.append(symbols[random_index])

easy_password_list = ran_letters + ran_symbols + ran_numbers

easy_password =""
for letter in easy_password_list:
  easy_password += letter
print(easy_password)
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

#randomly create password from easy password list
hard_password_list  = []

for number in range (0, len(easy_password_list)):
  random_index = random.randint(0, len(easy_password_list)-1)
  #we will pop a random index item from easy_password_list and add it to the hard_password_list until the easy_password_list is empty
  hard_password_list.append(easy_password_list.pop(random_index))

hard_password = ""
for letter in hard_password_list:
  hard_password += letter
print(hard_password)