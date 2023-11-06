class Bank:

    # class variables
    no_of_customers = 0
    account_no = 145768
    Error_message = {"Technical Error.Try again later."}

    # dundar method
    def __init__(self, name, last_name, mob_no, pin, initial_amount):
        # instance variables
        self.name = name
        self.last_name = last_name
        self.mobile_no = mob_no
        self.pin = pin
        self.bal_amount = initial_amount
        Bank.no_of_customers = Bank.no_of_customers + 1
        Bank.account_no = Bank.account_no + 3

        # self.menu()

    # def bank_details(self):
    #     print(f"Bank Name:SBI, Address: Pune, IFSC code:")

    def user_details(self):
        print(f"user_name: {self.name}\nlast_name: {self.last_name}\nmobile_number: {self.mobile_no}\nAccount number: {Bank.account_no}\nInitial_amount: {self.bal_amount}")

    # def create_account(self):


    def deposit_amount(self):
        Amount = float(input("Enter the Amount to deposit: "))
        if Amount > 0:
            self.bal_amount = self.bal_amount + Amount
            print("Transaction Completed. your current Balance is: ", self.bal_amount)
        else:
            print(self.Error_message)

    def withdraw_amount(self):
        Amount = float(input("Enter the Amount to withdraw: "))
        if Amount < self.bal_amount:
            self.bal_amount = self.bal_amount - Amount
            print("Transaction Completed. your current Balance is: ", self.bal_amount)
        else:
            print(self.Error_message)

    def make_payment(self, other):
        Phone_no = int(input("Enter the Phone number of recipient: "))
        if Phone_no == other.mobile_no:
            Amount = float(input("Enter the Amount to be transmitted: "))
            if Amount < self.bal_amount:
                self.bal_amount = self.bal_amount - Amount
                other.bal_amount = other.bal_amount + Amount
                print("Transaction Completed. Your current Balance is:", {self.bal_amount})
            else:
                print("Insufficient amount Balance")

        else:
            print("Enter the correct Phone number")

    def check_balance(self):
        phone_number = int(input("Enter Your phone: "))
        if phone_number == self.mobile_no:
            pin = int(input("Enter your pin: "))
            if pin == self.pin:
                print("your current balance is: ", self.bal_amount)
            else:
                print("Enter correct pin")
        else:
            print("Enter the correct Phone number")


    # def menu(self):
    #     user_input = """
    #             Hello user, how would you like to proceed
    #             1. press 1 to create new user
    #             2. press 2 for Existing user
    #             3. press 3
    #     """


customer1 = Bank("Mohit", "Sharma", 9854632174, 2547, 200)
customer2 = Bank("Rani", "Bhosle", 9745683215, 5544, 200)

print(Bank.no_of_customers)

customer1.user_details()
customer1.deposit_amount()
customer1.withdraw_amount()
customer1.make_payment(customer2)
customer1.check_balance()
customer2.check_balance()











