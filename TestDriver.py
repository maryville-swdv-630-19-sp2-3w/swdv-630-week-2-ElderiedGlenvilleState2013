from CheckingAccount import *


bank = CheckingAccount('El , Mckinney', '3234 drive, michigan', 23445, 200, 100)

print(bank.name)
print(bank.address)

bankBalance = bank.balance(500,200)
print(bankBalance)
print(bank.rewardsPoints(bankBalance))
