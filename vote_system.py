# import required libraries
import pandas as pd

# create a list of candidates
candidates = ['Candidate A', 'Candidate B', 'Candidate C']

# create a dictionary to store the vote counts for each candidate
votes = {}

# initialize the vote counts to zero for each candidate
for candidate in candidates:
    votes[candidate] = 0

# define a function to handle voting
def vote(candidate):
    if candidate in candidates:
        votes[candidate] += 1
        print(f'Thank you for voting for {candidate}!')
    else:
        print('Invalid candidate.')

# define a function to display the current vote counts
def display_votes():
    df = pd.DataFrame(list(votes.items()), columns=['Candidate', 'Votes'])
    print(df)

# main loop
while True:
    print('Welcome to the Voting System!')
    print('Please select your candidate:')
    for i, candidate in enumerate(candidates):
        print(f'{i+1}. {candidate}')
    print('Enter "0" to display the current vote counts.')
    print('Enter "exit" to quit.')
    choice = input('> ')
    if choice == 'exit':
        break
    elif choice == '0':
        display_votes()
    elif choice.isdigit() and int(choice) >= 1 and int(choice) <= len(candidates):
        vote(candidates[int(choice)-1])
    else:
        print('Invalid input.')
