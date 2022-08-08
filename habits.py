import random
import json
import ast
import time
import sys
import pandas

#global values

class Habits():
    def __init__(self):
        self.hardTasks = 0
        self.mediumTasks = 0
        self.easyTasks = 0
        self.reminders = 0
        self.pomodoros = 0
        self.remsMultiplier = 0
        self.pomsMultiplier = 0
        self.diffMultiplier = 0
        self.medMultiplier = 0
        self.easyMultiplier = 0
        self.name = 0
        self.experience = 0
        self.level = 0
        self.strength = 0
        self.balance = 0
        self.bossName = 0
        self.health = 0
        self.maxHealth = 0
        self.reward = 0

        self.openValues()

    def openValues(self):

        ## READ MULTIPLIER VALUES
        dataFile = open("data.txt", "r+")
        values = dataFile.read().split(",")
        #values


        self.hardTasks = int(float(values[0]))
        self.mediumTasks = int(float(values[1]))
        self.easyTasks = int(float(values[2]))
        self.reminders = int(float(values[3]))
        self.pomodoros = int(float(values[4]))
        #multipliers
        self.remsMultiplier = float(values[5])
        self.pomsMultiplier = float(values[6])
        self.diffMultiplier = float(values[7])
        self.medMultiplier = float(values[8])
        self.easyMultiplier = float(values[9])

        ## READ PLAYER INFORMATION
        playerFile = open("player.txt", "r+")
        values = playerFile.read().split(",")

        self.name = str(values[0])
        self.experience = float(values[1])
        self.level = int(float(values[2]))
        self.strength = float(values[3])
        self.balance = int(float(values[4]))


        ## READ BOSS FILES
        bossFile = open("boss.txt", "r+")
        values = bossFile.read().split(",")

        self.bossName = str(values[0])
        self.health = float(values[1])
        self.maxHealth = float(values[2])
        self.reward = int(values[3])

        self.homeScreen()

    def homeScreen(self):
        # choice = input("Would you like to enter tasks {1} or go to spends {2} or would you like to just see values {3}?\nExit == 4\n")
        print("\033[1;32m What would you like to do?\033[0m")
        choice = input("\n\tEnter Tasks: \t1\n\tGo to Spends: \t2\n\tSee Values: \t3\n\tBoss Values: \t4\n\tShop: \t5\n\tExit: \t6\n\n")
        print("\033c", end="")
        choice = int(choice)
        if(choice == 1 ):
            self.inputs()
            self.homeScreen()
            self.writeValues()
        elif(choice == 2):
            self.spends()
            self.homeScreen()
            self.writeValues()
        elif(choice == 3):
            self.fullPrint()
            self.homeScreen()
            self.writeValues()
        elif(choice == 4):
            self.bossValues()
            self.homeScreen()
            self.writeValues()
        elif(choice == 5):
            self.shop()
            self.homeScreen()
            self.writeValues()
        elif(choice == 6):
            self.balancePrint()
            print("\n")
            print("\033[1;35m /***************************************************/\n")
            print("\t\033[1;32mThank you for using this service!\n")
            print("\033[1;35m/***************************************************/\033[0m\n")
            self.writeValues()
            sys.exit()
        else:
            print("INVALID CHOICE, EXITING PROGRAM") #change color
            self.writeValues()
            sys.exit()

    def inputs(self):

        numDif = int(input("\033[0;36mPlease enter the number of difficult complexity tasks you have completed\n\t"))
        numMed = int(input("Please enter the number of medium complexity tasks you have completed\n\t"))
        numEas = int(input("Please enter the number of low complexity tasks you have completed\n\t"))
        numRem = int(input("Please enter the number of reminders you have completed\n\t"))
        numPom = int(input("Please enter the number of pomodoros you have completed\n\t"))
        print("\033[0;0m \033c", end="")


        diffGold = (numDif * float(self.diffMultiplier)) + numDif
        medGold = numMed * float(self.medMultiplier) + numMed
        easGold = numEas * float(self.easyMultiplier) + numEas
        remGold = numRem * float(self.remsMultiplier) + numRem
        pomGold = numPom * float(self.pomsMultiplier) + numPom

        totalGold = diffGold + medGold + easGold + remGold + pomGold # calculating total gold earned this time
        #change values

        self.experience += totalGold
        self.balance += totalGold #adding to current balance
        self.hardTasks += numDif
        self.mediumTasks += numMed
        self.easyTasks += numEas
        self.reminders += numRem
        self.pomodoros += numPom



        print("You just earned: ",round(totalGold,0)," gold!")
        self.checkLevel()
        self.bossUpdate(totalGold)

    def checkLevel(self):
        tempLevel = self.experience / (25*self.level)
        if(tempLevel > self.level):
            print("WOW! You have leveled up! Now you're level: ",self.level+1,"\n")
            self.level += 1
            multiplierIncrease = random.random()
            self.diffMultiplier += (multiplierIncrease/150)
            self.medMultiplier += (multiplierIncrease/250)
            self.easyMultiplier += (multiplierIncrease/350)
            self.remsMultiplier += (multiplierIncrease/450)
            self.pomsMultiplier += (multiplierIncrease/450)
            self.strength += (multiplierIncrease/100)

    def bossValues(self):
        print("You're currently fighting: \033[0;31m",self.bossName,"\033[0m \n")
        print("There is a bounty of: \033[1;33m",round(self.reward,0),"\033[0m on the boss' head")
        self.healthPrint()

    def bossUpdate(self,totalToday):
        self.health -= (self.strength * float(totalToday/(52))+ self.strength)
        print("You just did ",round(self.strength * float(totalToday/52) + self.strength, 3)," damage to ",self.bossName)

        if(self.health <= 0):
            print("\033[42myou have defeated the boss,",self.bossName,"!")
            self.balance += totalToday
            print("You have now recieved your reward\033[0m\n\nPlease update the boss.txt file")
            self.balancePrint()

    def spends(self):
        spendFile = open("spends.txt","r")
        spends = spendFile.read()
        spends = ast.literal_eval(spends)
        response = input("\033[1;32mWhat would you like to do?\033[1;0m\n\tSpend Gold? \t{1}\n\tAdd New Spends? \t{2}?\n")
        print("\033c", end="")
        if (int(response) == 1):
            self.spendGold()
        elif(int(response) == 2):
            self.changeSpends()

    def spendGold(self):
        spendFile = open("spends.txt", "r")
        spendString = spendFile.read()
        spends = ast.literal_eval(spendString)
        for item in spends:
            print(item, "costs \033[3m\033[1;31m", spends[item], "\033[0m\n")
        print("\nWhat would you like to buy?\nRemember, your current gold balance is: \033[5m\033[1;33m",self.balance,"\033[0m\n")
        amount = input()

        if(amount.find(",") != -1):
            amount = amount.split(",")
        for item in amount:
            contains = False
            for key, cost in spends.items():
                if(item == key[0]):
                    contains = True
                    if(cost <= self.balance):
                        val = key.partition("-")[2]
                        print("You just bought: \033[5m\033[1;33m", val, "\033[0m\nEnjoy!\n")
                        self.balance -= cost
                    else:
                        print("\033[5m\033[1;33mSorry, insufficient funds\033[0m")

    def changeSpends(self):
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

    def shop(self):
        fileVal = pandas.read_csv("shop.txt", sep=",", header=0, index_col=None)
        print(fileVal)
        print("\nWhat would you like to buy?\nRemember, your current gold balance is: \033[5m\033[1;33m",self.balance,"\033[0m\n")
        number = input("Enter the Item Number that you would like to purchase\n")
        if(int(number) > fileVal.shape[0]):
            print("Invalid choice, returning now to Home screen")
        else:
            print("This is what you selected\n")
            print(fileVal.iloc[[number]])
            if(self.balanceValid(fileVal.iloc[int(number), 1])):
                if(fileVal.iloc[int(number), 2]):
                    print("your strength has been increased by: ",fileVal.iloc[int(number), 3])
                    self.strength += int(fileVal.iloc[int(number), 3])
                    self.writeValues()
                else:
                    print("Boss has been damaged by: ",fileVal.iloc[int(number), 3])
                    self.health -= int(fileVal.iloc[int(number), 3])
                    self.writeValues()
                    self.checkBoss()
            else:
                pass

    def checkBoss(self):
        if(self.health <= 0):
            print("\033[42myou have defeated the boss,",self.bossName,"!")
            self.balance += reward
            print("You have now recieved your reward\033[0m\n\nPlease update the boss.txt file")
            self.balancePrint()

    def balanceValid(self,cost):
        if(self.balance >= cost):
            print("Transaction Successful\n")
            self.balance -= cost
            return True
        else:
            print("insufficient Funds\n")
            return False

    def balancePrint(self):
        print("\033[1;35m/***************************************************/\033[0m\n")
        print("\033[1;33m\tYour current gold balance is: ",int(self.balance),"\n")
        print("\033[1;35m/***************************************************/\033[0m\n")

    def fullPrint(self):
        self.writeValues()
        self.openValues()
        self.balancePrint()
        print("\033[1;35m/***************************************************/\033[0m\n")
        print("\033[0;32m\t",self.name, "your strength currently is: ",round(self.strength),"\n")
        print("\tYou are currently Level: ", round(self.level),"\n")
        print("\tBoss,",self.bossName," is at health: ",round(health, 3),"HP\n")
        print("\tYour experience is: ", round(self.experience,3),"XP\n")
        print("\033[1;35m/***************************************************/\033[0m\n")
        print("\033[1;35m/***************************************************/\033[0m\n")
        print("\033[0;36m\tYou've completed", self.hardTasks,"hard tasks\n")
        print("\tYou've completed", self.mediumTasks,"medium tasks\n")
        print("\tYou've completed", self.easyTasks,"easy tasks\n")
        print("\tYou've completed", self.reminders,"reminders\n")
        print("\tYou've completed", self.pomodoros,"pomodoros\n")
        print("\tYour current remsMultiplier is", self.remsMultiplier,"\n")
        print("\tYour current pomsMultiplier is", self.pomsMultiplier,"\n")
        print("\tYour current diffMultiplier is", self.diffMultiplier,"\n")
        print("\tYour current medMultiplier is", self.medMultiplier,"\n")
        print("\tYour current easyMultiplier is", self.easyMultiplier,"\n")
        print("\033[1;35m/***************************************************/\033[0m\n")

    def healthPrint(self):
        dashConvert = int(self.maxHealth/30)
        currentDashes = int(self.health/dashConvert)
        remainingHealth = 30 - currentDashes

        healthDisplay = '\N{Batak Symbol Bindu Na Metek}' * currentDashes
        remainingDisplay = ' ' * remainingHealth
        percent = str(int((self.health/self.maxHealth)*100)) + "%"

        print("\033[1;33m|" + healthDisplay + remainingDisplay + "|")
        print("         " + percent + "\033[0m")

    def writeValues(self):
        dataFile = open("data.txt", "w")
        dataValues = [self.hardTasks,self.mediumTasks,self.easyTasks,self.reminders,self.pomodoros,self.remsMultiplier,self.pomsMultiplier,self.diffMultiplier,self.medMultiplier,self.easyMultiplier]
        dataFile.seek(0)  # sets  point at the beginning of the file
        dataFile.truncate()  # Clear previous content
        for element in dataValues :
            string = str(element)+","
            dataFile.write(string)
        dataFile.close()

        playerFile = open("player.txt", "w")
        playerValues = [self.name,self.experience,self.level,self.strength,self.balance]
        playerFile.seek(0)  # sets  point at the beginning of the file
        playerFile.truncate()  # Clear previous content
        for element in playerValues :
            string = str(element)+","
            playerFile.write(string)
        playerFile.close()

        bossFile = open("boss.txt", "w")
        bossValues = [self.bossName,self.health,self.maxHealth,self.reward]
        bossFile.seek(0)  # sets  point at the beginning of the file
        bossFile.truncate()  # Clear previous content
        for element in bossValues :
            string = str(element)+","
            bossFile.write(string)
        bossFile.close()




Habits()
