# class Customers:
#     bankname= "HDFS Bank"
    
#     def __init__(self, name, account_no,balance=0.0):
#         self.name= name
#         self.account_no = account_no
#         self.balance= balance
    
#     def make_deposit(self):
#         amount=float(input("Enter amount to be deposited:"))
#         self.balance+= amount
#         print ("Current balance:", self.balance)
    
#     def make_withdrawal(self):
#         amount=float(input("Enter amount to withdraw:"))
#         if self.balance> amount:
#             self.balance-= amount
#             print("Current balance:",self.balance)
#         else:
#             print("You have insufficient balance")
    
#     def check_balance(self):
#         print("Current balance:", self.balance)
       
# print("Dear Customers,")
# print("Welcome to", Customers.bankname)
# name= input("Enter your name:")
# account_no=int(input("Enter your account no:"))
# bank= Customers(name, account_no)

# while True:
#     print("d-deposit\n w-withdrawal\n b-check_balance\n e-exit")
#     options= input("Enter the operation to perform:").lower()
#     if options== "d":
#         bank.make_deposit()
#     elif options=="w":
#         bank.make_withdrawal()
#     elif options=="b":
#         bank.check_balance()
#     elif options=="e":
#         break
#     else:
#         print("The given input is irrelavent")


# class bankstatement():
#     bankname= "HDFS Bank"  
    
#     def __init__(self,name,account_no,balance=0.0):
#         self.name= name
#         self.account_no= account_no
#         self.balance= balance

#     def deposit(self,amount):
#         self.amount= amount
#         self.balance+= amount
#         print("The amount deposited:",amount)
#         print("Current balance:",self.balance)

#     def withdraw(self,amount):
#         if amount> self.balance:
#             print("Insufficient balance")
#         else:
#             self.balance-=amount
#             print("Amount withdraw:",amount)
#             print("Current balance:", self.balance)

#     def balance(self):
#         print("Current balance:",self.balance)

# print("Welcome to",bankstatement.bankname)

# name=input("Enter your name:")
# account_no= int(input("Enter your account no:"))

# data=bankstatement(name,account_no)

# while True:
#     print("d-deposit\nw-withdraw\nb-balance\ne-exit")
#     options=input("Enter the options to be performed:")
    
#     if options=="d":
#         amount= float(input("Enter amount to deposit:"))
#         data.deposit(amount)
#     elif options=="w":
#         amount= float(input("Enter amount to withdraw: "))
#         data.withdraw(amount)
#     elif options=="b":
#         data.balance()
#     elif options=="e":
#         break
#     else:
#         print("The given output is irrelavent")



    



