from datetime import datetime
# lowest accepted temp, highest accepted temp, current temp, user set temp

temperature = [0, 20, 16, 15]
activeFridge = list()

def userOpenFridge(currentUser):
    file.write(f"{time},{activeFridge[0]},{currentUser},Fridge was opened.\n")
    print(f"{time},{activeFridge[0]},{currentUser},Fridge was opened.\n")

def openFridge():
    file.write(f"{time},Fridge X,System Alert,Fridge was opened.\n")
    print(f"{time},Fridge X,System Alert,Fridge was opened.\n")

def fridgeIsOpen():
    file.write(f"{time},Fridge X,System Alert,ALERT! - Fridge is still open\n")
    print(f"ALERT! - Fridge is still open at {time}\n")

def userCloseFridge(currentUser):
    file.write(f"{time},{activeFridge[0]},{currentUser},Fridge was closed.\n")
    print(f"Fridge was closed at {time} by {currentUser}\n")

def closeFridge():
    file.write(f"{time},Fridge X,System Alert,Fridge was closed.\n")
    print(f"Fridge was closed at {time}\n")

def userChangeTemp(currentUser):
    temperature[3] = (int(input(('What would you like the temperature to be: '))))
    file.write(f"{time},{activeFridge[0]},{currentUser},Temperature was changed to {temperature[3]}\n")
    print(f"Temperature was changed to {temperature[3]} at {time} by {currentUser}\n")

    if temperature[0] <= temperature[3] <= temperature[1]:
        temperature[2] = temperature[3]
    else:
        temperature[2] = temperature[3]
        file.write(f"{time},{activeFridge[0]},System Alert,ALERT! - Temperature has fallen outside of designated range to {temperature[3]}\n")
        print(f"ALERT! - Temperature has fallen outside of designated ({temperature[0]} - {temperature[1]}) to {temperature[3]} at {time}\n")
def changeTemp(temp):
    file.write(f"{time},Fridge X,System Alert,Temperature was changed to {temp}\n")
    print(f"Temperature was changed to {temp} at {time}\n")

    if temperature[0] <= temp <= temperature[1]:
        pass
    else:
        file.write(f"{time},Fridge X,System Alert,ALERT! - Temperature has fallen outside of designated range to {temp}\n")
        print(f"ALERT! - Temperature has fallen outside of designated range to {temp} at {time}\n")

def userCheckTemp(currentUser):
    file.write(f"{time},{activeFridge[0]},{currentUser}, Temperature Check: Temperature is {temperature[2]}.\n")
    print(f"Temperature is {temperature[2]} at {time}. Checked by {currentUser}\n")


def checkTemp():
    file.write(f"{time},Fridge X,System Alert,Temperature is {temperature[2]}. \n")
    print(f"Temperature is {temperature[2]} at {time}.\n")

    if temperature[3] == temperature[2]:
        pass
    else:
        file.write(f"{time},Fridge X,System Alert,ALERT! - Temperature sensor may be offline/broken. User-set temperature is not the actual temperature.\n")
        print(f"{time},ALERT! - Temperature sensor may be offline/broken. User-set temperature is not the actual temperature.\n")



def deviceOffline():
    file.write(f"{time},Fridge X,System Alert,ALERT! - There is no log data. The device may be offline.\n")
    print(f"{time},ALERT! - There is no log data. The device may be offline.\n")

def fridgeFunctionsMenu(currentUser):
    userInput = 0
    while userInput != -1:
        # print(f"[1] Open Fridge")
        print(f"[1] Close Fridge")
        print(f"[2] Change Temperature")
        print(f"[3] Check Temperature")
        print(f"[-1] Exit\n")
        userInput = int(input("Please select an option: "))

        # if userInput == 1:
        #   userOpenFridge(currentUser)
        if userInput == 1:
            userCloseFridge(currentUser)
        elif userInput == 2:
            userChangeTemp(currentUser)
        elif userInput == 3:
            userCheckTemp(currentUser)

def selectFridge(currentUser):
    count = 0
    for key, value in fridgesAndContent.items():
        count += 1
        print(f'[{count}] {key}: {value}')

    userInput = int(input(('Please select a fridge: ')))

    key_list = list(fridgesAndContent.keys())

    if len(activeFridge) == 1:
        activeFridge.pop(0)

    if userInput == 1:
        activeFridge.append(key_list[0])
    elif userInput == 2:
        activeFridge.append(key_list[1])
    elif userInput == 3:
        activeFridge.append(key_list[2])
    elif userInput == 4:
        activeFridge.append(key_list[3])

    fridgeFunctionsMenu(currentUser)

time = datetime.now()
file = open("hackNCATLog.csv", "a")

fridgesAndContent = {
    'Fridge 1':'Sprites',
    'Fridge 2':'Vaccines',
    'Fridge 3':'Potions',
    'Fridge 4':'Magic Wands'
}

