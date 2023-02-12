import tkinter as tk
from tkinter import messagebox
import random

def RockPaperScissors():
    def play_game(user_choice):
        computer_choice = random.choice(["rock", "paper", "scissors"])
        result = None
        if user_choice == computer_choice:
            result = "tie"
        elif user_choice == "rock":
            if computer_choice == "paper":
                result = "computer"
            else:
                result = "user"
        elif user_choice == "paper":
            if computer_choice == "scissors":
                result = "computer"
            else:
                result = "user"
        elif user_choice == "scissors":
            if computer_choice == "rock":
                result = "computer"
            else:
                result = "user"
        
        if result == "tie":
            message = "Tie! Both players chose " + computer_choice + "."
        elif result == "computer":
            message = "You lose! Computer chose " + computer_choice + "."
        else:
            message = "You win! Computer chose " + computer_choice + "."
        
        messagebox.showinfo("Result", message)
    
    root = tk.Tk()
    root.title("Rock Paper Scissors")
    root.geometry("200x200")
    
    rock_button = tk.Button(root, text="Rock", command=lambda: play_game("rock"))
    rock_button.pack()
    
    paper_button = tk.Button(root, text="Paper", command=lambda: play_game("paper"))
    paper_button.pack()
    
    scissors_button = tk.Button(root, text="Scissors", command=lambda: play_game("scissors"))
    scissors_button.pack()
    
    root.mainloop()

if __name__ == '__main__':
    RockPaperScissors()
