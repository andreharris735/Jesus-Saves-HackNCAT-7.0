from datetime import datetime

# The password is checked. The user has three attempts to authenticate.
def passwordCheck():
    counter = 0
    name = input('Please enter your username: ')
    password = input('Please enter your password: ')
    print()
    while counter <= 1:
        if name in passwordDict:
            if passwordDict[name] == password:
                print(f'Welcome, {name}!\n')
                file.write(f"{time},Fridge Not Yet Selected,{name}, {name} has logged in.\n")
                return name
                break
            else:
                counter += 1
                print('Invalid username/password. Please try again:')
                file.write(f"{time},Fridge X,System Alert,ALERT! - {name} has attempted to log in.\n")
                name = input('Please enter your username: ')
                password = input('Please enter your password: ')
                print()
        else:
            counter += 1
            print('Invalid username/password. Please try again:')
            file.write(f"{time},Fridge X,System Alert,ALERT! - {name} has attempted to log in.\n")
            name = input('Please enter your username: ')
            password = input('Please enter your password: ')
            print()
    else:
        print('Too many attempts. Please try again later.')
        file.write(f"{time},Fridge X,System Alert,ALERT! - {name} has attempted to log in.\n")
        exit()

# This allows the user to change their password, although still in development.
def changePassword(currentUser, passwordDict):
    password = input("Please enter your existing password")
    count = 0
    while count < 3:
        if password == passwordDict[currentUser]:
            passwordDict[currentUser] = input('Please enter your new password: ')
            return passwordDict
            break
        else:
            count += 1
            print('Please try again.')
            password = input('Please enter your existing password: ')
    else:
        print('Too many attempts. Please try again later.')
        exit()

def userFunctionsMenu(currentUser):
    userInput = 0
    while userInput != -1:
        print("[1] Change Password")
        print("[2] Change Username")
        print("[3] Delete User")
        print("[-1] Exit\n")
        userInput = int(input("Please select an option: "))

# This is a dictionary of allowed users and their passwords.

passwordDict = {
    'Bob': 'abc',
    'Abby': '123',
    'Barny': 'password'
}

# The program uses the datetime import to the current date and time for log entries and appends log entries to the hackNCATLog spreadsheet.
time = datetime.now()
file = open("hackNCATLog.csv", "a")



