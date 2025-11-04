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
        
class Customer:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        
    def edit_profile(self, name, age, city, pin, estate):
        self.name = name
        self.age = age
        self.address.change_address(city, pin, estate)

class Address:
    def __init__(self, city, pin, state):
        self.city = city
        self.pin = pin
        self.state = state

    def change_address(self, city, pin, state):
        self.city = city
        self.pin = pin
        self.state = state
        
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def login(self):
        print(f"{self.username} logged in")

    def register(self):
        print(f"{self.username} has register")

class Student:
    def __init__(self, student_id, courses):
        self.student_id = student_id
        self.courses = courses

    def enroll(self):
        print(f"Student {self.student_id} has enrolled in courses")

    def review(self):
        print(f"Student {self.student_id} is revewing courses")

class StudentUser(User, Student):
    def __init__(self, username, email, student_id, courses):
        User.__init__(self, username, email)
        Student.__init__(self, student_id, courses)

class Animal:
    def speak(self):
        print("speaking")

class Dog(Animal):
    def bark(self):
        print("barking")

class Bulldog(Dog):
    def guard(self):
        print("guarding")


class Calculator:
    def add(self, a, b):
        return a + b
    
    def add(self, a, b, c):
        return a + b + c

#Polymorphism: method overloading not suported


calc = Calculator()
print(calc.add(2, 3, 4))
print(calc.add(2,4))