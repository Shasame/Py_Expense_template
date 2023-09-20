from PyInquirer import prompt
from user import get_user

expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"list",
        "name":"spender",
        "message":"New Expense - Spender: ",
        "choices": get_user()
    },
    {
        "type":"checkbox",
        "name":"people",
        "message":"Other people involved: ",
        "choices": [{'name':x} for x in get_user()]
    }

]



def new_expense(*args):
    infos = prompt(expense_questions)
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    fs = open("expenses_report.csv", "a")
    expense = f"{infos['amount']},{infos['label']},{infos['spender']}|"
    for person in infos['people']:
        expense += f"{person},"
    expense = expense[:-1]
    fs.write(f"{expense}\n")
    fs.close()
    print("Expense Added !")
    return True

def get_expenses():
    # This function should return the expenses
    # It should return a list of expenses

    fs = open("expenses_report.csv", "r")
    expenses = []
    for line in fs:
        expenses.append(line.strip())
    fs.close()
    return expenses


