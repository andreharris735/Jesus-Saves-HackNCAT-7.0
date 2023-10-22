import fridgeFunctions
import userFunctions

# This is the file that the user will use to start the program.

# The first task is checking the username and password to see if an authorized user is allowed.
currentUser = userFunctions.passwordCheck()

# If the user is authenticated, the home menu will display. 
# Depending on what option is selected various menus will then be selected.

userInput = 0
while userInput != -1:
    print(f"[1] Fridge Options")
    print(f"[2] User Options")
    print(f"[-1] Exit")
    userInput = int(input("Please select an option: "))

    if userInput == 1:
        fridgeFunctions.selectFridge(currentUser)
    elif userInput == 2:
        userFunctions.userFunctionsMenu(currentUser)
