#Elderied week 2 homework 

class CheckingAccount:
    
    def __init__(self, name, address, accountNumber, credit, debit):
        self.name = name 
        self.address = address
        self.credit = credit
        self.debit = debit
        charge = 0 
        
        
    
        
        



    def __accountNumber__(self):
        return self.accountNumber
    
    #displaying the balance total balance
    def balance(self, credit, debit):
        self.balance = 0 
        self.balance += (credit - debit)
        return self.balance
    
    #added rewards every time the user spend money
    def rewardsPoints(self, balance):
        self.rewards = 0
        addingBalance = balance
 
        if addingBalance > 0:
            self.rewards += 2
            print("your rewards balance is ", self.rewards)
        else:
            print("you can get rewards with you buy")
            
        
        return self.rewards
  
        



bank = CheckingAccount('El , Mckinney', '3234 drive, michigan', 23445, 200, 100)

print(bank.name)
print(bank.address)

bankBalance = bank.balance(500,200)
print(bankBalance)
print(bank.rewardsPoints(bankBalance))