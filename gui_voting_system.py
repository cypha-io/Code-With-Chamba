import tkinter as tk

class ATM:
    def __init__(self, master):
        self.master = master
        master.title("ATM")

        # Create labels and entry widgets for user authentication
        self.label_id = tk.Label(master, text="Enter your ID:")
        self.entry_id = tk.Entry(master)
        self.label_id.grid(row=0, column=0)
        self.entry_id.grid(row=0, column=1)

        self.label_pin = tk.Label(master, text="Enter your PIN:")
        self.entry_pin = tk.Entry(master, show="*")
        self.label_pin.grid(row=1, column=0)
        self.entry_pin.grid(row=1, column=1)

        self.button_login = tk.Button(master, text="Log in", command=self.authenticate)
        self.button_login.grid(row=2, column=0, columnspan=2)

        # Create labels and entry widgets for account information
        self.label_balance = tk.Label(master, text="Balance:")
        self.entry_balance = tk.Entry(master, state="readonly")
        self.label_balance.grid(row=3, column=0)
        self.entry_balance.grid(row=3, column=1)

        self.label_history = tk.Label(master, text="Transaction History:")
        self.text_history = tk.Text(master, height=5, width=30, state="disabled")
        self.label_history.grid(row=4, column=0)
        self.text_history.grid(row=4, column=1)

        # Create buttons for transactions
        self.button_withdraw = tk.Button(master, text="Withdraw", command=self.withdraw)
        self.button_deposit = tk.Button(master, text="Deposit", command=self.deposit)
        self.button_transfer = tk.Button(master, text="Transfer", command=self.transfer)
        self.button_inquiry = tk.Button(master, text="Inquiry", command=self.inquiry)
        self.button_withdraw.grid(row=5, column=0)
        self.button_deposit.grid(row=5, column=1)
        self.button_transfer.grid(row=6, column=0)
        self.button_inquiry.grid(row=6, column=1)

        # Create buttons for receipts and exit
        self.button_print = tk.Button(master, text="Print Receipt", command=self.print_receipt)
        self.button_exit = tk.Button(master, text="Exit", command=master.quit)
        self.button_print.grid(row=7, column=0)
        self.button_exit.grid(row=7, column=1)

        # Initialize account balance and transaction history
        self.balance = 1000
        self.history = []

    def authenticate(self):
        id = self.entry_id.get()
        pin = self.entry_pin
