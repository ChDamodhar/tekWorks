class Payment:
    def __init__(self,amount):
        self.__amount=amount
    def getAmt(self):
        return self.__amount
        
    def pay(self):
        pass
    
class CashPay(Payment):
    def pay(self):
        print(f"Paid Rs.{self.getAmt()} in cash")

class Credit_debitPay(Payment):
    def pay(self):
        print(f"Paid Rs.{self.getAmt()} in Credit/debit")

class UPIPay(Payment):
    def pay(self):
        print(f"Paid Rs.{self.getAmt()} in UPI")

Payments=[CashPay(1000),Credit_debitPay(1000),UPIPay(1000)]
for i in Payments:
    i.pay()


        

