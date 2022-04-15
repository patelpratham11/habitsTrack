import random
import json
import ast
import time
import sys

#setting up global variables
#reading file
file = open("data.txt", "r+")
values = file.read().split(",")
#setting up global variables/ multipliers
maxMultiplier = float(values[6])
remsMultiplier = float(values[7])
pomsMultiplier = float(values[8])
diffMultiplier = float(values[9])
medMultiplier = float(values[10])
easyMultiplier = float(values[11])

#first executed method
def first():
    # choice = input("Would you like to enter tasks {1} or go to spends {2} or would you like to just see values {3}?\nExit == 4\n")
    print("\033[1;32m What would you like to do?\033[0m")
    choice = input("\n\tEnter Tasks: \t1\n\tGo to Spends: \t2\n\tSee Values: \t3\n\tExit: \t4\n\n")
    print("\033c", end="")
    choice = int(choice)
    if(choice == 1 ):
        inputs()
        gold()
    elif(choice == 2):
        spend()
        first()
    elif(choice == 3):
        fullView()
    elif(choice == 4):
        gold()
        print("\n")
        print("\033[1;35m /***************************************************/\n")
        print("\tThank you for using this service!\n")
        print("/***************************************************/\033[0m\n")
        sys.exit()
    else:
        print("INVALID CHOICE, EXITING PROGRAM") #change color
        sys.exit()

#taking in inputs and then updating gold based on multipliers
def inputs():
    dif = int(input("\033[0;36mPlease enter the number of difficult complexity tasks you have completed\n\t"))
    me = int(input("Please enter the number of medium complexity tasks you have completed\n\t"))
    eas = int(input("Please enter the number of low complexity tasks you have completed\n\t"))
    rem = int(input("Please enter the number of reminders you have completed\n\t"))
    pom = int(input("Please enter the number of pomodoros you have completed\n\t"))
    print("\033[0;0m \033c", end="")
    diff = dif * float(diffMultiplier) + dif
    med = me * float(medMultiplier)+ me
    easy = eas * float(easyMultiplier)+ eas
    rems = (int(values[3])*float(remsMultiplier)*rem) + rem
    poms = (int(values[4])*float(pomsMultiplier)*pom) + pom
    total = easy+med+diff+rems+poms
    multiplier = random.uniform(0.1,maxMultiplier)
    total = int(total*multiplier+(total/2))
    write(diff, med, easy, rems, poms, total)

#changing all values then writing them to a file
def write(diff, med, easy, rems, poms, total):
    values.pop()
    values[0] = int(int(values[0])+diff)
    values[1] = int(int(values[1])+med)
    values[2] = int(int(values[2])+easy)
    values[3] = int(int(values[3])+rems)
    values[4] = int(int(values[4])+poms)
    values[5] = int(int(values[5])+total)
    values[6] = float(values[6])
    values[7] = float(values[7])
    values[8] = float(values[8])
    values[9] = float(values[9])
    values[10] = float(values[10])
    values[11] = float(values[11])
    if(int(int(values[5])/5) != 0):
        value = float(values[5]/5)
        values[6] = round((values[6]* value /3700)+ values[6],4)
    if(int(int(values[0])/5) != 0):
        value = float(values[0]/5)
        values[9] = round((values[9]* value /3700)+ values[9],4)
    if(int(int(values[1])/5) != 0):
        value = float(values[1]/5)
        values[10] = round((values[10]* value /3700)+ values[10],4)
    if(int(int(values[2])/5) != 0):
        value = float(values[2]/5)
        values[11] = round((values[11]* value /3700)+ values[11],4)
    if(int(int(values[3])/5) != 0):
        value = float(values[3]/5)
        values[7] = round((values[7]* value /3700)+ values[7],4)
    if(int(int(values[4])/5) != 0):
        value = float(values[4]/5)
        values[8] = round((values[8]* value /3700)+ values[8],4)


    fullView()
    finalPrint()

#spendings list; adding or spending
def spend():
    spendFile = open("spends.txt","r")
    spends = spendFile.read()
    spends = ast.literal_eval(spends)
    response = input("\033[1;32mWhat would you like to do?\033[1;0m\n\tSpend Gold? \t{1}\n\tAdd New Spends? \t{2}?\n")
    print("\033c", end="")
    if (int(response) == 1):
        for item in spends:
            print(item, "costs \033[3m\033[1;31m", spends[item], "\033[0m\n")
        msg = "\nHow much are you spending?\nRemember, your current gold balance is: \033[5m\033[1;33m"+str(values[5])+"\033[0m\n"
        amount = input(msg)
        print("\033c", end="")

        if(amount.find(",") != -1):
            amount = amount.split(",")

        for item in amount:
            item = int(item)
            prize = ""
            if(item <= float(values[5])):
                values[5] = int(values[5])
                values[5] -= item
                for key, value in spends.items():
                    if item == value:
                        prize = key
                        print("You just bought: \033[5m\033[1;33m", prize, "\033[0m\nEnjoy!\n")
                else:
                    print("Transaction complete but item not found. Please edit datafile if invalid Transaction.\n")
            else:
                print("\033[5m\033[1;33mSorry, insufficient funds\033[0m")
    if(int(response) == 2):
        spendFile = open("spends.txt","w")
        responseTwo = int(input("Are you editing?\n\t\033[1;32mYes \t{1}\033[0m\033[1;31m\n\tNo \t{2}\033[0m\n"))
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
                name = input("What is the name?\n")
                cost = input("What is the cost?\n")
                cost = int(cost)
                spends[name]=cost
            spendFile.write(str(spends))
    print("\033c", end="")
    finalPrint()

#adding everything to the document
def finalPrint():
    file.close()
    fileNew = open("data.txt", "w")
    for value in values:
        fileNew.write(str(value)+",")
#simple bank balance
def gold():
    print("\033[1;35m/***************************************************/\033[0m\n")
    print("\033[1;33m\tYour current gold balance is: ",values[5],"\n")
    print("\033[1;35m/***************************************************/\033[0m\n")

#every single piece of information; gold; multipliers; streaks
def fullView():
    print("\033[1;35m/***************************************************/\033[0m\n")
    print("\033[0;32m\tYou've completed", values[0],"hard tasks\n")
    print("\tYou've completed", values[1],"medium tasks\n")
    print("\tYou've completed", values[2],"easy tasks\n")
    print("\tYou've completed", values[3],"reminders\n")
    print("\tYou've completed", values[4],"pomodoros\n")
    print("\033[1;35m/***************************************************/\033[0m\n")
    print("\033[1;35m/***************************************************/\033[0m\n")
    print("\033[0;36m\tYour current maxMultiplier is", values[6],"\n")
    print("\tYour current remsMultiplier is", values[7],"\n")
    print("\tYour current pomsMultiplier is", values[8],"\n")
    print("\tYour current diffMultiplier is", values[9],"\n")
    print("\tYour current medMultiplier is", values[10],"\n")
    print("\tYour current easyMultiplier is", values[11],"\n")
    print("\033[1;35m/***************************************************/\033[0m\n")
    gold()
    first()

first()
