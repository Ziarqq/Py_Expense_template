from PyInquirer import prompt
from status import add_expense_to_status
from checks import NumberValidator, StringValidator
import csv

def get_user_list(answers):
    user_list = []
    with open('users.csv', 'r') as users:
        reader = csv.reader(users)
        for row in reader:
            user_list.append(row[0])
    return user_list

def get_involved_list(answers):
    involved_list = []
    user_list = []
    with open('users.csv', 'r') as users:
        reader = csv.reader(users)
        for row in reader:
            user_list.append(row[0])
    
    for user in user_list:
        if user == answers["spender"]:
            involved_list.append({'name':user, 'checked':True})
        else:
            involved_list.append({'name':user})

    return involved_list


expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
        "validate": NumberValidator,
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
        "validate": StringValidator,
    },
    {
        "type":"list",
        "name":"spender",
        "message":"New Expense - Spender: ",
        "choices": get_user_list,
    },
    {
        "type":"checkbox",
        "name":"involved",
        "message":"New Expense - Involved people: ",
        "choices": get_involved_list,
    },
]
def new_expense(*args):
    infos = prompt(expense_questions)

    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    with open('expense_report.csv', 'a') as expenses:
        writer = csv.writer(expenses)
        writer.writerow('')
        writer.writerow([infos["amount"]] + [infos["label"]] + [infos["spender"]])
    
    add_expense_to_status(infos)
    print("Expense Added !")
    return True


