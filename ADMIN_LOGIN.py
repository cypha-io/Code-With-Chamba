import getpass
import time
import hashlib

print('Follow the instructions below carefully')
print('Admin || Guest User')
choice = input('Login As: ')


#Code to check if person is entering as a user or an admin
if (choice == 'Admin' or 'admin'):
    name = input('Enter your name:\n')
    password = getpass.getpass()
    password_input = hashlib.sha256(password.encode()).hexdigest()
    stored_password = password

    if (name == 'chamba' or name == 'Chamba' and password == stored_password):
        print('Loading....')
        time.sleep(2)
        print('Welcome,', name)

#change this to fit Assigned Teammates tomorrow
        ass_wrk = 'You have no assigned work'
        opt_1 = ass_wrk
        opt_2 =  'No available members. Thank you.'
    while True:    
        print('1. Check Assigned Work. Thank you.')
        print('2. Check Team Members')
        print('3. Exit')
        option = int(input('Select your option: '))
        if (option == 1):
            print(opt_1)
            print('----------------------------------------')
        elif(option == 2):
            print(opt_2)
            print('----------------------------------------')
        elif(option == 3):
            break
        else:
            print('Error!')
    else:
        print('Invalid name or passoword')
else:
    print('Kindly try again soon...')