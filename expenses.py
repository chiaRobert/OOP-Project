import uuid
from datetime import datetime, timezone
#from main import expense,expenseDatabase

class Expense:
  def __init__(self, title, amount):
    self.title = title
    self.amount = amount
    self.id = str(uuid.uuid1())
    self.created_at = datetime.now(timezone.utc)
    self.updated_at = datetime.now(timezone.utc)
    
  def update(self, title=None, amount=None):
      #remember to update self.updated_at using datetime.utcnow()
    if title:
        self.title = title
    if amount is not None:
        self.amount = amount
    self.updated_at = datetime.now(timezone.utc)  
 
  def to_dict(self):
      
          expense_list = {"Id": id, "Title": self.title, "Amount": self.amount, "Created at": self.created_at.isoformat, "Updated at": self.updated_at.isoformat}
          print(expense_list)

class ExpenseDatabase:
  def __init__(self):
    self.expenses = []
     
    
  def add_expense(self, expense):
    self.expenses.append(expense)
    #expenses.append(Expense("Groceries", 5400))
    #expenses.append(Expense("Tuition", 25600))


  def remove_expense(self, expense_id):
    self.expenses = [expense for expense in self.expenses if expense.id != expense_id]
    
  def get_expense_by_id(self, expense_id):
    for expense in self.expenses:
        if expense.id == expense_id:
            return expense
    return None
    
  def get_expense_by_title(self, expense_title):
    return[expense for expense in self.expenses if expense.title.lower() == expense_title.lower()]
    
  def to_dict(self):  
    return[expense.to_dict() for expense in self.expenses]
      
      
# Create the database
dbase = ExpenseDatabase()

expense1 = Expense("Utilities", 180.44)
expense2 = Expense("Phone Bill", 200.85)
dbase.add_expense(expense1)
dbase.add_expense(expense2)

# Update an expense
expense1.update(amount=95.76)

# Retrieve by ID
expense = dbase.get_expense_by_id(expense1.id)
print(expense.to_dict())


# Retrieve by title
utilities_expenses = dbase.get_expense_by_title("Utilities")
for expense in utilities_expenses:

    print(expense.to_dict())

# Remove an expense
dbase.remove_expense(expense2.id)


# Get all expenses in dict format
total_expenses = dbase.to_dict()

print(total_expenses)











