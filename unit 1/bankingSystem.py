class JordanFirstBank():
    def __init__(self, name, age, balance, acountNumber, address, phoneNumber):
        self.name = name
        self.age = age
        self.balance = balance
        self.acountNumber = acountNumber
        self.adress = address
        self.phoneNumber = phoneNumber


        def deposit(self, balance, amount):
            self.balance += amount
            print('you have' + str(self.balance))

        def withdrawl(self, balance, amount):
            sefl.balance -= amount
            print('you have' + str(self.balnce))

        def checkBalance(self):
             print('you have' + str(self.balance))


acount_1 = JordanFirstBank('Kobe', 24, 300000, 3467, '23chestnut',  2678908648,)
acount_2 = JordanFirstBank('Wardell',37, 42300000, 8904, 'ebhkuek', 18005883200)

acount_1.checkBalance()
acount_1.deposit(500)
acount_1.withdrawl(200)

acount_2.checkBalance()

acount_2.deposit(700)

acount_2.withdrawl(100)