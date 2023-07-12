#parent class user
#child class bank

class User():
    
    def __init__(self, name,gender,age):
        name = self.name
        gender =self.gender
        age =self.age
    
    def details(self):
        print('name is ', self.name)
        print('my gender is ', self.gender)
        print('my age is ', self.age )
        
class Bank(User):
    def __init__(self,name,gender,age):
        super(User, self).__init__(name , age,gender)
        self.balance = 0
        
        def deposit(self,amount):
            self.amount = amount
            self.balance =self.balance +self.amount
            print('your new balance has been updated and is ksh ',self.balance )
            
        def withdrawal(self,amount):
            self.amount = amount
            balance =self.balance
            if self.balance > self.amount:
                print('you cannot withdraw these funds,you have insufficient funds your balance is ', self.balance)
            else: 
                self.balance = self.balance  - self.amount
                print('your new balance is ',self.balance) 