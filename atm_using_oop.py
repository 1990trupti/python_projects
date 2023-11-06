class Atm:

    # static/class variable
    counter = 1
    #constructor
    #special/magic/ Tundar method
    def __init__(self):
        # Instance variable
        self.pin = ""    # __ means we will hind the object i.e private data
        self.balance = 0
        self.sno = Atm.counter
        Atm.counter = Atm.counter + 1

        self.menu()

    @staticmethod
    def get_counter(self):
        return Atm.counter

    @staticmethod
    def set_counter(self, new):
        if type(new) == int:
            Atm.counter = new
        else:
            print("Not allowed")

    def menu(self):
        user_input = input("""
                    Hello. how would you like to proceed?
                    1. Enter 1 to create pin
                    2. Enter 2 to deposit
                    3. Enter 3 to withdraw
                    4. Enter 4 to check balance
                    5. Enter 5 to exit
        """)
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        else:
            print("Bye")

    def create_pin(self):
        self.pin = input("Enter your pin")
        print("Pin set successfully")

    def deposit(self):
        temp = input("Enter your pin")
        if temp == self.pin:
            amount = int(input("Enter the amount to deposit: "))
            self.balance = self.balance + amount
            print("Deposit Successful")
        else:
            print("Invalid pin")

    def withdraw(self):
        temp = input("Enter your pin")
        if temp == self.pin:
            amount = int(input("Enter the amount to withdraw: "))
            if self.balance > amount:
                self.balance = self.balance - amount
                print("Withdraw successful")
            else:
                print("Insufficient fund")
        else:
            print("Invalid pin")

    def check_balance(self):
        temp = input("Enter your pin")
        if temp == self.pin:
            print(self.balance)
        else:
            print("Invalid pin")


sbi = Atm()
# print(sbi)

# print(sbi.create_pin())
print(sbi.deposit())
print(sbi.withdraw())
print(sbi.check_balance())
c1 = Atm()
c2 = Atm()
c1.sno







