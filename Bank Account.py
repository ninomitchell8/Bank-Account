class Account():

    def __init__(self,owner,balance = 0):

        self.owner = owner
        self.balance = balance

    def deposit(self,deposit_amount):

        self.balance = self.balance + deposit_amount

        print(f'Added {deposit_amount} to your balance')


    def withdrawal(self,withdrawal_amount):

        if self.balance >= withdrawal_amount:
            self.balance = self.balance - withdrawal_amount
            print(f'You have withdrawn {withdrawal_amount} from your account.')

        else:
            ('Sorry you do not have enough funds!!!')

    def __str__(self):
        return f' {self.owner} your balance is: {self.balance}'
















