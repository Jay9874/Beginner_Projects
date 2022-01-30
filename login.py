import time


username = 'Jay'
password = 'kuchhbhi'

username_input = input('Username: ')
password_input = input('Password: ')

if username_input == username and password_input == password:
    print('Access Granted')
    print('OK')
    time.sleep(5)
    print('Please wait')
    time.sleep(1)
    print('Loading....')
    time.sleep(1)
    print('...')
    time.sleep(1)
    print('...')
    print('Alright you have security clearance. Pulling uo the secret mainframe')


elif username_input != username and password_input == password:
    print('Wrong Username')

elif username_input == username and password_input != password:
    print('Wrong Password')

else :
    print('You might wanna check both fields....')



