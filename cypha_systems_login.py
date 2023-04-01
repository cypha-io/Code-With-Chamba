import getpass
import time
import hashlib


print('Welcome To Cypha Python Systems')
print('Please Wait...')
time.sleep(3)

error = 'User details denied'
team = ['Chamba', 'Alice', 'Ama']
opt_2 =  len(team)
stored_password = 'admin123'

#Assigment of works
curent_work = []
ass_wrk = curent_work



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
                ask_work = input('Do you want to start work?\n')
                if (ask_work == 'Yes' or ask_work == 'YES' or ask_work == 'yes'):
                    add_work = input('Enter your prefared work: ')
                    curent_work.append(add_work)
                    print('Your current work is/are: ',curent_work)
                    print('----------------------------------------')
                    
                elif (curent_work == []):
                        print('----------------------------------------')
                        print('You have no active works available')
                        print('----------------------------------------')
                        
                else:
                        print('test run success')
            elif(option == 2):
                print('Please wait...')
                time.sleep(2)
                print('----------------------------------------')
                print('You have', opt_2, 'members currently')
                ask_mem = input('Do you want to add a member?\n')
                if (ask_mem == 'Yes' or ask_mem == 'yes' or ask_mem == 'YES'):
                    add_mem = input('New Member Name: ')
                    team.append(add_mem)
                else:
                    print('Okay, no members will be added')
                    print('----------------------------------------')
                ask_if = input('Do you want to list them? ')
                if (ask_if == 'Y' or ask_if == "y" or ask_if == 'Yes' or ask_if == 'yes' or ask_if == 'YES'):
                    print('Your team members are:', team)
                else:
                    print('----------------------------------------')
                    print('Okay, no members will be listed')
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
    



