import getpass
import hashlib

print('Follow the instructions below carefully')
choice = input('Login Or Register?\n')


if (choice == 'register' or 'Register'):
    name = input('Enter your name:\n')
    password = getpass.getpass()
    password_input = hashlib.sha256(password.encode()).hexdigest()
    stored_password = password

    if (name == 'chamba' or name == 'Chamba' and password == stored_password):
        print('Loading....')
        print('Welcome,', name)
        print('Your password is:', password)

        balance = 1000
        opt_1 = balance
        opt_2 = 'Your registered name is', name
        print('1. Check Balance')
        print('2. Check Name')
        option = int(input('Select your option\n'))
        if (option == 1):
            print('Your balance is', opt_1)
        else:
            print(opt_2)
    else:
        print('Invalid name or passoword')
else:
    print('Kindly try again soon...')