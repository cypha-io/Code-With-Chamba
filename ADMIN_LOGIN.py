import getpass
import hashlib

print('Follow the instructions below carefully')
choice = input('Admin Or User\n')

#Code to check if person is entering as a user or an admin
if (choice == 'Admin' or 'admin'):
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
        opt_2 =  name
        print('1. Check Balance')
        print('2. Check Name')
        option = int(input('Select your option\n'))
        if (option == 1):
            print('Your balance is', opt_1)
        elif(option == 2):
            print('Registered name is', opt_2)
        else:
            print('Error!')
    else:
        print('Invalid name or passoword')
else:
    print('Kindly try again soon...')