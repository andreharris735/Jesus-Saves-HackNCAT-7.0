from datetime import datetime
import fridgeFunctions

def gatherData(values):
    isFridgeOpen = False
    stepOne = line.split('\n')
    for i in stepOne:
        stepTwo = i.split(', ')
        for j in stepTwo:
            stepThree = j.split(':')
            values[stepThree[0][1:-1]].append(stepThree[1][2:-1])

    for i in range(len(values['sn'])):

        if values['event'][i] == 'temp':
            fridgeFunctions.changeTemp(float(values['value'][i]))

        elif (values['event'][i] == 'door'):
            isFridgeOpenCount = 0
            if (values['value'][i] == 'opened'):
                fridgeFunctions.openFridge()
                isFridgeOpen = True
            else:
                fridgeFunctions.closeFridge()
                isFridgeOpen = False

    if isFridgeOpen:
        fridgeFunctions.fridgeIsOpen()

readFile = open("sampledata.txt", "r")
writeFile = open("hackNCATLog.csv", "a")
time = datetime.now()
line = readFile.read()

values = {
    'sn': list(),
    'event':list(),
    'value':list()
}

if len(line) == 0:
    writeFile.write(f"{time},ALERT! - There is no data in the log file. The system may be powered off.\n")
    print(f"{time},ALERT! - There is no data in the log file. The system may be powered off.\n")
else:
    gatherData(values)

