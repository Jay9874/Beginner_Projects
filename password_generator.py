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


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

length_letter = len(letters)
length_numbers = len(numbers)
length_symbols = len(symbols)


#random_letter_list = []


letter_string = ""
symbol_string = ""
number_string = ""
for n in range (0, nr_letters):
  random_letters_range = random.randint(0, length_letter-1)
  random_letters_generator =letters[random_letters_range]

  letter_string += random_letters_generator
#print(letter_string)

for n in range (0, nr_symbols):
 random_symbol_range = random.randint(0, length_symbols-1)
 random_symbol_generator = symbols[random_symbol_range]
 symbol_string += random_symbol_generator
#print(symbol_string)

for n in range (0, nr_numbers):
 random_number_range = random.randint(0, length_numbers-1)
 random_number_generator = numbers[random_number_range]
 number_string += random_number_generator

#print(number_string)

print(f"Your generated password is : {letter_string}{symbol_string}{number_string}")

















 








