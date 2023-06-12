user = input('Enter a letter: ')

vowels = ['a', 'o', 'u', 'e', 'i', 'A', 'O', 'U', 'E', 'I']
consonansts = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z', 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y','z']

if (user in vowels):
    print('This is a vowel')
    user_num_1 = int(input('Enter a number: '))
    if (user_num_1 % 2) == 0:
        print('This is an even number')
    else:
        print('This is an odd number')
elif (user in consonansts):
    print('This is a consonansts')
    user_num_2 = int(input('Enter a number: '))
    if (user_num_2 < 0):
        print('The number is a negative number')
    else:
        print('The number is a positive number')
else: 
    print('Error 404!')
    
