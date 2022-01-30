import random
import time 

def guess(x):
     random_number =  random.randint(1, x)
     guess = 0
     while guess != random_number:
         guess = int(input(f'Guess a number between 1 and {x}: '))
         
         if guess < random_number:
             time.sleep(1)
             print('Sorry, guess again with higher values')
         elif guess > random_number:
             time.sleep(1)
             print('Sorry, try with lesser value')
             
     print(f'Congrats! you did it. You guessed the number {random_number} ') 

guess(10)