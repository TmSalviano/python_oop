import sys

class Atm:
    
    __counter = 1    
    
    def __init__(self):
        self.__pin = ""
        self.__balance = 0
        self.serialno = Atm.__counter
        Atm.__counter += 1
        self.__menu()
        
    @staticmethod
    def get_counter():
        return Atm.__counter
    
    def set_counter(new):
        if type(new) == int:
            Atm.__counter = new
        else:
            print("Not allowed")

    
    def get_pin(self):
        return self.__pin
    
    def set_pin(self, new_pin):
        if type(new_pin) == str:
            self.__pin = new_pin
            print("Changed")
        else:
            print("not allowe")
        
    def __menu(self):
        while True:
            i = input("""
                Choose action:
                1. Set pin
                2. Deposit
                3. Withdraw
                4. check balance
                5. exit 
                """)
            if i == "1":
                self.set_pin()
            elif i == "2":
                self.deposit()
            elif i == "3":
                self.withdraw()
            elif i == "4":
                self.check_balance()
            else:
                sys.exit()

    def set_pin(self):
        pin = input("Set pin:")
        self.__pin = pin

    def deposit(self):
        answer = input("Type pin:")
        if answer == self.__pin:
            amount = int(input("Type amount: "))
            self.__balance += amount
        else:
            print("Wrong pin")

    def withdraw(self):
        answer = input("Type pin:")
        if answer == self.__pin and self.__balance > 0:
            amount = int(input("Type amount: "))
            self.__balance -= amount
        else:
            print("Wrong pin")

    def check_balance(self):
        print(self.__balance)
        
obj = Atm()