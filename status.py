from expense import get_expenses
from user import get_user

def get_status():
    status = {}
    expenses = get_expenses()
    users = get_user()
    for user in users:
        status[user] = 0
    for expense in expenses:
        amount, label, spender, owner = expense.split(",")
        status[spender] += float(amount)
    print("Status:")
    for user in status:
        print(f"{user} : {status[user]}")
    return
