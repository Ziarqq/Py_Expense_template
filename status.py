from PyInquirer import prompt
import csv

def get_status():
    expenses = []
    with open('status.csv', 'r') as status_file:
        reader = csv.reader(status_file)
        for row in reader:
            expenses.append(row[0])
    return expenses

def add_expense_to_status(infos):
    total = infos["amount"]
    spender = infos["spender"]
    people_involved = infos["involved"]
    number_of_parts = len(people_involved)
    payment_per_person = int(total) / number_of_parts

    report = []
    for person in people_involved:
        if person == spender:
            report.append([spender + " owes nothing"])
        else:
            report.append([person + " owes " + str(payment_per_person) + " to " + spender])

    with open('status.csv', 'a', newline='') as status_file:
        writer = csv.writer(status_file)
        writer.writerows(report)

def display_status():
    status = get_status()
    for line in status:
        print(line)
