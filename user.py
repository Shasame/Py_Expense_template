from PyInquirer import prompt
user_questions = [
    {
        "type":"input",
        "name":"Name",
        "message":"New User - Name:",
    },

]

def add_user():
    # This function should create a new user, asking for its name
    infos = prompt(user_questions)
    fs = open("users.csv", "a")
    fs.write(f"{infos['Name']}\n")
    print("User Added !")    
    return

def get_user():
    # This function should return the user name
    # If there is more than one user, it should ask the user to choose one

    userList = []
    fs = open("users.csv", "r")
    for line in fs:
        userList.append(line.strip())
    fs.close()
    return userList