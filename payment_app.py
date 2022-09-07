class PaymentApp:
    # Python Class init function.
    def __init__(self, usernames):
        self.accounts = {username: 0 for username in usernames}

    # Adding users to the payment app.
    def add_user(self, username):
        self.accounts[username] = 0

    # Users depositing money into the app.
    def deposit(self, username, amount):
        self.accounts[username] += amount

    # Users checking their balance.
    def get_balance(self, username):
        return self.accounts[username]

    #  Users sending money to other app users
    def transfer(self, sender, recipient, amount):
        if self.accounts[sender] < amount:
            raise Exception(f"{sender} has insufficient balance")

        self.accounts[sender] -= amount
        self.accounts[recipient] += amount

    # Users transfering their money out of the app.
    def withdraw(self, username, amount):
        if self.accounts[username] < amount:
            raise Exception(f"{username} has insufficient funds to withdraw")
        self.accounts[username] -= amount
