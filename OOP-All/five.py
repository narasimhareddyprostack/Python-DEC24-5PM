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

#How to access class members - using ref var or object
a1=Account()
a1.open_account()
a1.deposit_amount()
a1.withdrawl_amount()
a1.get_bal()
a1.close_account()
