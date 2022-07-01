class Account:
    
    def __init__(self, filepath):
        self.filepath=filepath
        with open(filepath, 'r') as file:
            self.balance=int(file.read())
            
    def withdraw(self, amount):
        self.balance=self.balance - amount
        
    def deposit(self, amount):      # local variable amount i nema veze sa amount u withdraw metodu
        self.balance=self.balance + amount
        
    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))
            
            
class Checking(Account):
    
    def __init__(self, filepath, fee):
        super().__init__(filepath)
        self.fee=fee
        
    def transfer(self, amount):
        self.balance=self.balance - amount -self.fee
        
checking=Checking("26_ObjectOrientedProgrammingOOP//balance.txt", 1)
print(checking.balance)
checking.deposit(10)
checking.transfer(110)
print(checking.balance)
checking.commit()
print(checking.balance)

            
            
#account=Account("26_ObjectOrientedProgrammingOOP//balance.txt")
#print(account.balance)
## account.withdraw(100)
## account.deposit(1000)
#print(account.balance)
#account.commit()
