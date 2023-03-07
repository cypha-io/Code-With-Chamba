import getpass
import time
import hashlib


print('Welcome To Cypha Python Systems')
print('Please Wait...')
time.sleep(3)

error = 'Error 404'
ass_wrk = 'You have no assigned work'
opt_2 =  'No available members. Thank you.'
stored_password = 'admin123'

choice = input('Login As: ')


if (choice == 'Admin' or 'admin'):
    name = input('Enter your name:\n')
    password = getpass.getpass()
    password_input = hashlib.sha256(password.encode()).hexdigest()






if (name == 'chamba' or name == 'nartey'  and password == stored_password):
        print('Loading....')
        time.sleep(2)
        print('Welcome,', name)
        while True:    
            print('1. Check Assigned Work')
            print('2. Check Team Members')
            print('3. Password')
            print('4. Exit')
            option = int(input('Select your option: '))
            if (option == 1):
                print('Please wait...')
                time.sleep(2)
                print('----------------------------------------')
                print(ass_wrk)
                print('----------------------------------------')
            elif(option == 2):
                print('Please wait...')
                time.sleep(2)
                print('----------------------------------------')
                print(opt_2)
                print('----------------------------------------')
            elif(option == 3):
                print('Please wait...')
                time.sleep(3)
                while True:
                    print('----------------------------------------')
                    print('1. Check Password')
                    print('2. Reset Password')
                    print('3. Exit')
                    pass_ = int(input('Select your option: '))
                    if(pass_ == 1):
                        print('----------------------------------------')
                        print('Please wait...')
                        time.sleep(2)
                        print('----------------------------------------')
                        print('Your current password is:', password)
                        print('----------------------------------------')
                    elif(pass_ == 3):
                        break
                
            elif(option == 4):
                print('----------------------------------------')
                print('Exiting Please Wait....')
                time.sleep(3)
                break
            else:
                print('Error!')
else:
        print('Invalid Username Or Password')
    
