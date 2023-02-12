import getpass
import time
import hashlib


print('Welcome To Cypha Python Systems')
print('Please Wait...')
time.sleep(3)

choice = input('Login As: ')


if (choice == 'Admin' or 'admin'):
    name = input('Enter your name:\n')
    password = getpass.getpass()
    password_input = hashlib.sha256(password.encode()).hexdigest()
    stored_password = password

    if (name == True  and password == stored_password):
        print('Loading....')
        time.sleep(2)
        print('Welcome,', name)
        ass_wrk = 'You have no assigned work'
        opt_1 = ass_wrk
        opt_2 =  'No available members. Thank you.'
    while True:    
        print('1. Check Assigned Work')
        print('2. Check Team Members')
        print('3. Password')
        print('4. Exit')
        option = int(input('Select your option: '))
        if (option == 1):
            time.sleep(3)
            print(opt_1)
            print('----------------------------------------')
        elif(option == 2):
            time.sleep(3)
            print(opt_2)
            print('----------------------------------------')
        elif(option == 3):
            time.sleep(3)
            print('1. Check Password')
            print('2. Reset Password')
            pass_ = int(input('Select your option: '))
            if(pass_ == 1):
                time.sleep(3)
                print('Your current password is:', password)
            
        elif(option == 4):
            print('Exiting Please Wait....')
            time.sleep(5)
            break
        else:
            print('Error!')
    else:
        print('Invalid name or passoword')
