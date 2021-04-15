"Create a Budget class that can instantiate "
"objects based on different budget categories"
"1. Depositing funds to each of the categories"
"2. Withdrawing funds from each category"
"3. Computing category balances"
"4. Transferring balance amounts between categories"



class Budget:
    
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    
    def deposit(self, amount):
        
        
        old_balance = self.balance
        self.balance = self.balance + amount
        
        return f"Old: {old_balance}, New:{self.balance}"
    
    def withdraw(self, amount):
        old_balance = self.balance
        
        if self.balance < amount:
            return "You don't have enough cash"
        else:
            self.balance = self.balance - amount
            
            return f"Old: {old_balance}, New:{self.balance}"
    
    def get_balance(self):
        feedback = f"Your balance is {self.balance}"
        
        return feedback
    
    def transfer(self, amount, transfer_to):
        if self.balance < amount:
            return "You don't have enough cash"
        else:
            self.balance = self.balance - amount
            transfer_to.balance = transfer_to.balance + amount
            
            feedback = f"You transferred ${amount} to {transfer_to.name} budget\n"
            feedback += f"The balance for {self.name} is now {self.balance} while\n"
            feedback += f"The balance for {transfer_to.name} is now {transfer_to.balance}"
            
            return feedback
        
        
        
    
    
food_budget = Budget("food", 2000)
clothing_budget = Budget("clothing", 5000)
entertainment_budget = Budget("entertainment", 3000)

food_budget.deposit(1000)

food_budget.withdraw(1500)


print(food_budget.transfer(500, clothing_budget))

print(food_budget.get_balance())
print(clothing_budget.get_balance())
print(entertainment_budget.get_balance())

   