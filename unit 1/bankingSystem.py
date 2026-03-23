# import random

# class JordanFirstBank():
#     def __init__(self, name, age, balance, acountNumber, address, phone):
#         self.name = name
#         self.age = age
#         self.balance = balance
#         self.acountNumber = acountNumber
#         self.adress = address
#         self.phoneNumber = phone

#         def deposit(self, amount):
#             self.balance += amount
#             print('you have' + str(self.balance))

#         def withdrawl(self, amount):
#             self.balance -= amount
#             print('you have' + str(self.balnce))

#         def checkBalance(self):
#              print('you have' + str(self.balance))

# acount_1 = JordanFirstBank('Kobe', 24, 300000, 3467, '23chestnut',  2678908648,)
# acount_2 = JordanFirstBank('Wardell',37, 42300000, 8904, 'ebhkuek', 18005883200)

# acount_1.checkBalance()
# acount_1.deposit(500)
# acount_1.withdrawl(200)

# acount_2.checkBalance()
# acount_2.deposit(700)
# acount_2.withdrawl(100)

# bankUsers = []


def CreateAccount():
    print("Welcome to Jordan Fisrt Bank")
    print("Please complete the form to create an account")
    name = input("please type in your name: ")
    age = int(input("please tyepe in your age: "))
    accountNumber = random.randrange(100,500)
    

    balance = int(input("please type in how much you want to deposit: "))
    print("Congrats! Your accout is complete")
    account = JordanFirstBank(name, age, balance, accountNumber, 'na')
    return

CreateAccount()


def mainBankAccount():
    print("Welcome")
    print("are you an existing customer?")
    print("Pleas type 1 for existing and 2 for new member: ")
    answer = input()
    if answer == 1:
        print("Welceome back")
    elif answer == 2:
        createaccount()

mainBankAccount()
