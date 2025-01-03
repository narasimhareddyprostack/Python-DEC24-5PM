class Account:
    acc_min_bal = 500
    branch_name='Marathahalli'

    def open_account(self):
        print("Account Opened Successfully")
    def deposit_amount(self):
        print("Amount Deposited")
    def withdrawl_amount(self):
        print("Low Balance")
    def get_bal(self):
        print("Server busy")
    def close_account(self):
        print("Bal is -ve! Please deposit more")