class Account: 
    def __init__(self): 
        self.balance=0
        print("Hello!!!Welcome to Deposit&Withdrawl Machine") 
  
    def deposit(self): 
        amount=float(input("Enter amount to be Deposited:40000 ")) 
        self.balance += amount 
        print("40000:",amount) 
  
    def withdraw(self): 
        amount = float(input("Enter amount to be Withdrawed: ")) 
        if self.balance>=amount: 
            self.balance-=amount 
            print("3000: amount") 
        else: 
            print("0.00 Insufficient balance  ") 
  
    def display(self): 
        print("\n Net Available Balance=",self.balance) 
  