import random
import json
import ast
import time
import sys

#global values


#values
hardTasks = 0
mediumTasks = 0
easyTasks = 0
reminders = 0
pomodoros = 0
#multipliers
maxMultiplier = 0
remsMultiplier = 0
pomsMultiplier = 0
diffMultiplier = 0
medMultiplier = 0
easyMultiplier = 0

#player
name = 0
experience = 0
level = 0
strength = 0
balance = 0

## READ BOSS FILES
bossName = 0
health = 0
reward = 0

def openValues():

    ## READ MULTIPLIER VALUES
    dataFile = open("data.txt", "r+")
    values = dataFile.read().split(",")
    #values
    global hardTasks
    global mediumTask
    global easyTasks
    global reminders
    global pomodoros
    global maxMultiplier
    global remsMultiplier
    global pomsMultiplier
    global diffMultiplier
    global medMultiplier
    global easyMultiplier
    global name
    global experience
    global level
    global strengt
    global balance
    global bossName
    global health
    global reward

    hardTasks = int(float(values[0]))
    mediumTasks = int(float(values[1]))
    easyTasks = int(float(values[2]))
    reminders = int(float(values[3]))
    pomodoros = int(float(values[4]))
    #multipliers
    maxMultiplier = float(values[5])
    remsMultiplier = float(values[6])
    pomsMultiplier = float(values[7])
    diffMultiplier = float(values[8])
    medMultiplier = float(values[9])
    easyMultiplier = float(values[10])

    ## READ PLAYER INFORMATION
    playerFile = open("player.txt", "r+")
    values = playerFile.read().split(",")

    name = str(values[0])
    experience = float(values[1])
    level = int(float(values[2]))
    strength = float(values[3])
    balance = int(float(values[4]))


    ## READ BOSS FILES
    bossFile = open("boss.txt", "r+")
    values = bossFile.read().split(",")

    bossName = str(values[0])
    health = float(values[1])
    reward = int(values[2])

def homeScreen():
    openValues()
    # choice = input("Would you like to enter tasks {1} or go to spends {2} or would you like to just see values {3}?\nExit == 4\n")
    print("\033[1;32m What would you like to do?\033[0m")
    choice = input("\n\tEnter Tasks: \t1\n\tGo to Spends: \t2\n\tSee Values: \t3\n\tBoss Values: \t4\n\tExit: \t5\n\n")
    print("\033c", end="")
    choice = int(choice)
    if(choice == 1 ):
        inputs()
        homeScreen()
    elif(choice == 2):
        spends()
        homeScreen()
    elif(choice == 3):
        fullPrint()
        homeScreen()
    elif(choice == 4):
        bossValues()
        homeScreen()
    elif(choice == 5):
        balancePrint()
        print("\n")
        print("\033[1;35m /***************************************************/\n")
        print("\t\033[1;32mThank you for using this service!\n")
        print("\033[1;35m/***************************************************/\033[0m\n")
        sys.exit()
    else:
        print("INVALID CHOICE, EXITING PROGRAM") #change color
        sys.exit()

def inputs():
    openValues()

    numDif = int(input("\033[0;36mPlease enter the number of difficult complexity tasks you have completed\n\t"))
    numMed = int(input("Please enter the number of medium complexity tasks you have completed\n\t"))
    numEas = int(input("Please enter the number of low complexity tasks you have completed\n\t"))
    numRem = int(input("Please enter the number of reminders you have completed\n\t"))
    numPom = int(input("Please enter the number of pomodoros you have completed\n\t"))
    print("\033[0;0m \033c", end="")


    diffGold = (numDif * float(diffMultiplier)) + numDif
    medGold = numMed * float(medMultiplier) + numMed
    easGold = numEas * float(easyMultiplier) + numEas
    remGold = numRem * float(remsMultiplier) + numRem
    pomGold = numPom * float(pomsMultiplier) + numPom

    totalGold = diffGold + medGold + easGold + remGold + pomGold # calculating total gold earned this time
    #change values
    global experience
    global balance
    global hardTasks
    global mediumTasks
    global easyTasks
    global reminders
    global pomodoros

    experience += totalGold
    balance += totalGold #adding to current balance
    hardTasks += numDif
    mediumTasks += numMed
    easyTasks += numEas
    reminders += numRem
    pomodoros += numPom



    checkLevel()
    bossUpdate(totalGold)
    writeValues()

def checkLevel():
    global level
    global maxMultiplier
    global remsMultiplier
    global pomsMultiplier
    global diffMultiplier
    global medMultiplier
    global easyMultiplier
    global strength

    tempLevel = experience / 25
    if(tempLevel > level):
        print("WOW! You have leveled up! Now you're level: ",int(tempLevel),"\n")
        level = int(tempLevel)
        multiplierIncrease = random.random()
        diffMultiplier += multiplierIncrease
        medMultiplier += (multiplierIncrease/2)
        easyMultiplier += (multiplierIncrease/3)
        remsMultiplier += (multiplierIncrease/4)
        pomsMultiplier += (multiplierIncrease/4)
        strength += (multiplierIncrease/2)

def bossValues():
    print("You're currently fighting: \033[0;31m",bossName,"\033[0m \n")
    print("The boss is currently at: \033[5m\033[1;31m",round(health,3),"\033[0m health.")
    print("There is a bounty of: \033[1;33m",reward,"\033[0m on the boss' head")

def bossUpdate(totalToday):
    global health
    global strength
    global reward
    global balance

    health -= (strength * float(totalToday/3))
    print("You just did ",round(strength * totalToday/3, 3)," damage to ",bossName)
    if(health <= 0):
        print("\033[42myou have defeated the boss,",bossName,"!")
        balance += reward
        print("You have now recieved your reward\033[0m\n\nPlease update the boss.txt file")
        balancePrint()

def spends():
    spendFile = open("spends.txt","r")
    spends = spendFile.read()
    spends = ast.literal_eval(spends)
    response = input("\033[1;32mWhat would you like to do?\033[1;0m\n\tSpend Gold? \t{1}\n\tAdd New Spends? \t{2}?\n")
    print("\033c", end="")
    if (int(response) == 1):
        spendGold()
    elif(int(response) == 2):
        changeSpends()

def spendGold():
    global balance

    spendFile = open("spends.txt", "r")
    spendString = spendFile.read()
    spends = ast.literal_eval(spendString)
    for item in spends:
        print(item, "costs \033[3m\033[1;31m", spends[item], "\033[0m\n")
    print("\nWhat would you like to buy?\nRemember, your current gold balance is: \033[5m\033[1;33m",balance,"\033[0m\n")
    amount = input()

    if(amount.find(",") != -1):
        amount = amount.split(",")
    for item in amount:
        contains = False
        for key, cost in spends.items():
            if(item == key[0]):
                contains = True
                if(cost <= balance):
                    print("You just bought: \033[5m\033[1;33m", item, "\033[0m\nEnjoy!\n")
                    balance -= cost
                else:
                    print("\033[5m\033[1;33mSorry, insufficient funds\033[0m")
    # if (contains == False):
    #     print("ERROR")

def changeSpends():
    spendFile = open("spends.txt","r+")
    spendString = spendFile.read()
    spends = ast.literal_eval(spendString)
    responseTwo = int(input("Are you going to do?\n\t\033[1;32mEdit Existing Spends \t{1}\033[0m\033[1;31m\n\tAdd New Spends \t{2}\033[0m\n"))
    print("\033c", end="")
    if(responseTwo == 1):
        for item in spends:
            print(item, "costs", spends[item])
        edit = input("Which item are you editing? (Just enter the name as shown above)\n")
        newValue = int(input("Enter the new price\n"))
        spends[edit] = newValue
        print("Changed Successfully!\n")
        print("\033c", end="")
        for item in spends:
            print(item, "costs", spends[item])
    if (responseTwo == 2):
        repeats = input("How many spends are you adding?\n")
        repeats = int(repeats)
        for x in range(repeats):
            total = len(spends)
            name = input("What is the name? Don't forget to add 'number-' before the name\n")
            cost = input("What is the cost?\n")
            cost = int(cost)
            additional = str(total+1)+"-"
            name = additional+name
            spends[name]=cost
    spendFile.seek(0)  # sets  point at the beginning of the file
    spendFile.truncate()  # Clear previous content
    spendFile.write(str(spends))

def balancePrint():
    print("\033[1;35m/***************************************************/\033[0m\n")
    print("\033[1;33m\tYour current gold balance is: ",int(balance),"\n")
    print("\033[1;35m/***************************************************/\033[0m\n")

def fullPrint():
    balancePrint()
    print("\033[1;35m/***************************************************/\033[0m\n")
    print("\033[0;32m\tYou've completed", hardTasks,"hard tasks\n")
    print("\tYou've completed", mediumTasks,"medium tasks\n")
    print("\tYou've completed", easyTasks,"easy tasks\n")
    print("\tYou've completed", reminders,"reminders\n")
    print("\tYou've completed", pomodoros,"pomodoros\n")
    print("\033[1;35m/***************************************************/\033[0m\n")
    print("\033[1;35m/***************************************************/\033[0m\n")
    print("\033[0;36m\tYour current maxMultiplier is", maxMultiplier,"\n")
    print("\tYour current remsMultiplier is", remsMultiplier,"\n")
    print("\tYour current pomsMultiplier is", pomsMultiplier,"\n")
    print("\tYour current diffMultiplier is", diffMultiplier,"\n")
    print("\tYour current medMultiplier is", medMultiplier,"\n")
    print("\tYour current easyMultiplier is", easyMultiplier,"\n")
    print("\033[1;35m/***************************************************/\033[0m\n")

def writeValues():

    #values
    global hardTasks
    global mediumTask
    global easyTasks
    global reminders
    global pomodoros
    global maxMultiplier
    global remsMultiplier
    global pomsMultiplier
    global diffMultiplier
    global medMultiplier
    global easyMultiplier
    global name
    global experience
    global level
    global strengt
    global balance
    global bossName
    global health
    global reward

    dataFile = open("data.txt", "w")
    dataValues = [hardTasks,mediumTasks,easyTasks,reminders,pomodoros,maxMultiplier,remsMultiplier,pomsMultiplier,diffMultiplier,medMultiplier,easyMultiplier]
    dataFile.seek(0)  # sets  point at the beginning of the file
    dataFile.truncate()  # Clear previous content
    for element in dataValues :
        string = str(element)+","
        dataFile.write(string)
    dataFile.close()

    playerFile = open("player.txt", "w")
    playerValues = [name,experience,level,strength,balance]
    playerFile.seek(0)  # sets  point at the beginning of the file
    playerFile.truncate()  # Clear previous content
    for element in playerValues :
        string = str(element)+","
        playerFile.write(string)
    playerFile.close()

    bossFile = open("boss.txt", "w")
    bossValues = [bossName,health,reward]
    bossFile.seek(0)  # sets  point at the beginning of the file
    bossFile.truncate()  # Clear previous content
    for element in bossValues :
        string = str(element)+","
        bossFile.write(string)
    bossFile.close()



homeScreen()
