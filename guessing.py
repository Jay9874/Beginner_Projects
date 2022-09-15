
import random
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is {guess} too high(H), too low(L), or correct(C)??').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        elif feedback != "c" or feedback != 'l' or feedback != 'h':
            print('Entered wrong input, please enter a valid key')
    print(f'Yay! The Computer guessed your number, {guess}, correctly!')

computer_guess(10)

