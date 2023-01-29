import getpass
import hashlib

print('Follow the instructions below carefully')
choice = input('Login Or Register?')


if (choice == 'register' or 'Register'):
    name = input('Enter your name:\n')
    password = getpass.getpass()
    password_input = hashlib.sha256(password.encode()).hexdigest()
    stored_password = password

    if (name == 'chamba' or name == 'Chamba' and password == stored_password):
        print('Loading....')
        print('Welcome,', name)
        print('Your password is:', password)
    else:
        print('Invalid User,',name and password)


