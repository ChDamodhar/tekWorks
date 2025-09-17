class BankAcc:
    def __init__(self,balance=0):
        self.__balance=balance
    def deposit(self,amt):
        if (amt>0):
            self.__balance+=amt
        else:
            print("Amount should be positive")
    def withdraw(self,amt):
        if(amt>self.__balance):
            print("Insufficient balance")
        elif(amt<=0):
            print("Amount should be positive")
        else:
            self.__balance -= amt
    def get_balance(self):
        return self.__balance
b=BankAcc(200)
b.deposit(2000)
b.withdraw(500)
print(b.get_balance())
