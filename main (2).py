# function to withdraw the amount
def withdraw(self):
amount = float(input("Enter amount to be withdrawn:"))
if self.balance >=amount:
  self.balance -=amount
ptint("\n You Withdrew:",amount)
else:
print("\n Insufficient balance")