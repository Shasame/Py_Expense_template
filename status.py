from expense import get_expenses
from user import get_user

def get_status():
    status = {}
    expenses = get_expenses()
    users = get_user()
    for expense in expenses:
        spenderInfo, people = expense.split("|")
        amount, label, spender = spenderInfo.split(",")
        #for every expense calculate the amount of money all the other in people owe to spender
        if spender not in status:
            status[spender] = 0
        for person in people.split(","):
            if person not in status:
                status[person] = 0
            status[person] -= float(amount)/len(people.split(","))
        status[spender] += float(amount) - float(amount)/len(people.split(","))
    print("Users:")
    for user in status:
        print(f"{user} : {status[user]}")
    return
