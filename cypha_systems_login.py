import getpass
import time
import hashlib


print('Welcome To Cypha Python Systems')
print('Please Wait...')
time.sleep(3)

error = 'User details denied'
team = ['Chamba', 'Alice', 'Ama']
ass_wrk = 'You have no assigned work'
opt_2 =  len(team)
stored_password = 'admin123'



print('ADMIN | GUEST | ROOTUSER')
choice = input('>')


if (choice == 'Admin' or 'admin' or 'ADMIN'):
    name = input('Enter your name: ')
    password = getpass.getpass()
    password_input = hashlib.sha256(password.encode()).hexdigest()
else:
    print(error)
if password == stored_password:
    print('Details Accepted...')
    time.sleep(1)

    
    
        






    if (name == 'chamba'):
        print('Please Wait....')
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
                print('You have', opt_2, 'members currently')
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
                    elif (pass_ == 2):
                        print = 'What is your old password?'
                        new_pass = input('>')
                    if (new_pass == stored_password):
                        print('Just a moment')
                        
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
        print('Invalid Username')
elif password != stored_password:
    print(error)
    



