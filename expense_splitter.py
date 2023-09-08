class ExpenseSplitter:
    def __init__(self):
        self.participants = {}
        self.expenses = []
    
    def add_participant(self, name): 
        self.participants[name] = 0
        
    def add_expense(self, description, amount, payer, participants):
        self.expenses.append({
            'description' : description,
            'amount' : amount,
            'payer' : payer,
            'participants' : participants
        })
        
    def compute_owed_amount(self):     
        for expense in self.expenses:
            participant_amount = expense['amount'] / len(expense['participants'])
            for participant in expense['participants']:
                if participant != expense['payer']:
                    self.participants[participant] += participant_amount
                    
    def display_owed_amounts(self):
        for participant, amount_owed in self.participants.items():
            print(f'{participant} owes {amount_owed:.2f}')
                    
def main():
    #Invoke class
    expense_splitter = ExpenseSplitter()
    
     # Add participants
    expense_splitter.add_participant("Alice")
    expense_splitter.add_participant("Bob")
    expense_splitter.add_participant("Charlie")

    # Add expenses
    expense_splitter.add_expense("Dinner", 90, "Alice", ["Alice", "Bob", "Charlie"])
    expense_splitter.add_expense("Gas", 30, "Bob", ["Alice", "Bob"])
    expense_splitter.add_expense("Drinks", 20, "Alice", ["Alice", "Bob"])

    # Calculate and display owed amounts
    expense_splitter.compute_owed_amount()
    expense_splitter.display_owed_amounts()

if __name__ == '__main__':
    main()