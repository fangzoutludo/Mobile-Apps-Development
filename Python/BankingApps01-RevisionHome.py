# Parent Class
class User:

    # Here we will put all the arguments we want from our users
    def __init__(self, name, age, gender):

        # Here we have our three different properties assigned to our object
        self.name = name
        self.age = age
        self.gender = gender
        
    # With "self", I can have access to all the properties
    def show_details(self):
        print("Personal Details")
        print("")
        print("Name ", self.name)
        print("Age  ", self.age)
        print("Gender ", self.gender)


# Child Class
class Bank(User):
    def __init__(self, name, age, gender):

        # A "super()" avoids us having write the lines of code 16 to 18, it does it for us
        super().__init__(name, age, gender)

        # Stores details about the account balance
        self.balance = 0

    # Stores details about the amount that will allows me to deposit
    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Account balance has been updated : €", self.balance)

    # Stores details about the amount that will allows me to do the withdraw
    def withdraw(self,amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient Funds | Balance Available : €", self.balance)
        else:
            self.balance = self.balance - self.amount
            print("Account balance has been updated : €", self.balance)

    # Stores details about the amount that will allows me to see the users personal details
    def view_balance(self):
        self.show_details()
        print("Account balance: €", self.balance)
