#Elderied week 2 homework 

class CheckingAccount:
    
    def __init__(self, name, address, accountNumber, balance):
        self.name = name 
        self.address = address
        self.balance = balance
        self.accountNumber = accountNumber
        



    def accountNumber(self):
        return    self.accountNumber
    
    
    
    def credit(self):
        return self.credit
    
    
    def debit(self):
        return self.debit
    
    def __total__(self):
        return self.credit - self.debit
    
    #displaying the balance total balance
    def balance(self, total):
        return self.balance - self.total
    
  
        



bank = CheckingAccount('El , Mckinney', '3234 drive, michigan', 23445, 200)

print(bank.name)
print(bank.address)
print(bank.balance)