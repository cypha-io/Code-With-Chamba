import getpass
import time
import hashlib
from typing import List


def login() -> str:
    print('Welcome To Cypha Python Systems')
    print('Please Wait...')
    time.sleep(3)

    while True:
        choice = input('Login As: ').lower()
        if choice in ['admin']:
            return choice
        else:
            print('Invalid choice. Please try again.')


def authenticate(name: str, password: str, stored_password: str) -> bool:
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return name in ['chamba', 'nartey'] and hashed_password == stored_password


def check_assigned_work() -> str:
    return 'You have no assigned work'


def check_team_members() -> str:
    return 'No available members. Thank you.'


def check_password() -> str:
    return getpass.getpass()


def reset_password() -> None:
    print('Resetting password...')
    # Code to reset password


def main() -> None:
    stored_password = 'admin123'
    while True:
        choice = login()
        if choice == 'admin':
            name = input('Enter your name: ').lower()
            password = check_password()
            if authenticate(name, password, stored_password):
                print('Please Wait....')
                time.sleep(2)
                print(f'Welcome, {name.title()}')
                while True:
                    print('1. Check Assigned Work')
                    print('2. Check Team Members')
                    print('3. Password')
                    print('4. Exit')
                    option = int(input('Select your option: '))
                    if option == 1:
                        print('Please wait...')
                        time.sleep(2)
                        print('----------------------------------------')
                        print(check_assigned_work())
                        print('----------------------------------------')
                    elif option == 2:
                        print('Please wait...')
                        time.sleep(2)
                        print('----------------------------------------')
                        print(check_team_members())
                        print('----------------------------------------')
                    elif option == 3:
                        print('Please wait...')
                        time.sleep(3)
                        while True:
                            print('----------------------------------------')
                            print('1. Check Password')
                            print('2. Reset Password')
                            print('4. Exit')
                            pass_option = int(input('Select your option: '))
                            if pass_option == 1:
                                print('----------------------------------------')
                                print('Please wait...')
                                time.sleep(2)
                                print('----------------------------------------')
                                print('Your current password is:', password)
                                print('----------------------------------------')
                            elif pass_option == 2:
                                reset_password()
                            elif pass_option == 4:
                                break
                            else:
                                print('Invalid option. Please try again.')
                    elif option == 4:
                        print('----------------------------------------')
                        print('Exiting Please Wait....')
                        time.sleep(3)
                        break
                    else:
                        print('Invalid option. Please try again.')
            else:
                print('Invalid Username Or Password')


if __name__ == '__main__':
    main()
