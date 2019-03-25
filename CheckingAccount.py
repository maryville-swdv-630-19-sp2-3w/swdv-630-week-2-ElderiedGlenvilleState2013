#Elderied week 2 homework 

class CheckingAccount:
    
    def __init__(self, name, address, accountNumber,credit, debit, balance):
        self.name = name 
        self.address = address
        self.balance = balance
        self.accountNumber = accountNumber
        self.credit = credit
        self.debit = debit



    def accountNumber(self):
        return    self.accountNumber
    
    
    
    def credit(self):
        return self.credit
    
    
    def debit(self):
        return self.debit
    
    
    def balance(self, credit, debit):
        
        credit = self.credit
        debit = self.debit



