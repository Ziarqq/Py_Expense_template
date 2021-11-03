from PyInquirer import prompt
import csv

user_questions = [
    {
        "type":"input",
        "name":"Name",
        "message":"Username: ",
    }
]

def add_user(*args):
    infos = prompt(user_questions)

    # This function should create a new user, asking for its name
    with open('users.csv', 'a', newline='') as users_file:
        writer = csv.writer(users_file)
        writer.writerow([infos["Name"]])

    print("User added!")
    return True