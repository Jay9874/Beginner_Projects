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

letter_string = ""
symbol_string = ""
number_string = ""
password_string = ""

lett_lst = []
for n in range (0, nr_letters):
  random_letters_range = random.randint(0, length_letter-1)
  rand_lett_gen =letters[random_letters_range]
  lett_lst.append(rand_lett_gen)

for char in lett_lst:
  letter_string += char

sym_lst = []
for n in range (0, nr_symbols):
 random_symbol_range = random.randint(0, length_symbols-1)
 rand_sym_gen= symbols[random_symbol_range]
 sym_lst.append(rand_sym_gen)

for char in sym_lst:
  symbol_string += char
  
num_lst=[]
for n in range (0, nr_numbers):
 random_number_range = random.randint(0, length_numbers-1)
 rand_num_gen = numbers[random_number_range]
 num_lst.append(rand_num_gen)

for char in num_lst:
  number_string += char
  
print(f"\nYour generated password is : {letter_string}{symbol_string}{number_string}")


gen_pass_lst = num_lst + sym_lst +lett_lst
len_gen_pass_lst = len(gen_pass_lst) 

for n in range (0, len_gen_pass_lst):
  rand_char_range = random.randint(0, len_gen_pass_lst-1)
  rand_char_gen = gen_pass_lst[rand_char_range]
  password_string += rand_char_gen

print(f"Your randomised generated password is: {password_string}")



