import fridgeFunctions
import userFunctions


currentUser = userFunctions.passwordCheck()

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