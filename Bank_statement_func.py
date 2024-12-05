def balance(amount):
    print("Current balance:",amount)

def deposit(amount,balance):
    balance+= amount
    print("Amount deposited:", amount)
    print("Current balance:",balance)
    return balance

def withdraw(amount,balance):
    if balance>amount:
       balance-= amount
       print("Amount withdrew:",amount)
       print("Current balance:", balance)
    else:
        print("Insufficient balance")
    return balance

balance=0.0

amount=float(input("Enter amount to be deposited:"))
balance=deposit(amount,balance)

amount= float(input("Enter the amount to withdraw:"))
balance=withdraw(amount,balance)



