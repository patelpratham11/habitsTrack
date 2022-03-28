import random
import json
import ast
import time

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
    choice = input("Would you like to enter tasks {1} or go to spends {2} or would you like to just see values {3}?\nExit == 4\n")
    choice = int(choice)
    if(choice == 1 ):
        inputs()
        time.sleep(2)
        gold()
    if(choice == 2):
        spend()
        time.sleep(2)
        first()
    if(choice == 3):
        time.sleep(2)
        fullView()
    if(choice == 4):
        gold()
        print("Thank you for using this service!\n\n")

#taking in inputs and then updating gold based on multipliers
def inputs():
    dif = int(input("Please enter the number of difficult complexity tasks you have completed\n"))
    me = int(input("Please enter the number of medium complexity tasks you have completed\n"))
    eas = int(input("Please enter the number of low complexity tasks you have completed\n"))
    rem = int(input("Please enter the number of reminders you have completed\n"))
    pom = int(input("Please enter the number of pomodoros you have completed\n"))
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
    response = input("Do you want to spend {1} or do you want to add new spends {2}?\n")
    if (int(response) == 1):
        for item in spends:
            print(item, "costs", spends[item])
        msg = "How much are you spending?\nRemember, your current gold balance is: "+str(values[5])+"\n"
        amount = input(msg)
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
                print("You just bought:", prize, "Enjoy!\n")
            else:
                print("Sorry, insufficient funds")
    if(int(response) == 2):
        spendFile = open("spends.txt","w")
        responseTwo = int(input("Are you editing? Yes {1} or No {2}\n"))
        if(responseTwo == 1):
            for item in spends:
                print(item, "costs", spends[item])
            edit = input("Which item are you editing? (Just enter the name as shown above)\n")
            newValue = int(input("Enter the new price\n"))
            spends[edit] = newValue
            print("Changed Successfully!\n")
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
    finalPrint()

#adding everything to the document
def finalPrint():
    file.close()
    fileNew = open("data.txt", "w")
    for value in values:
        fileNew.write(str(value)+",")
#simple bank balance
def gold():
    print("################################################\n")
    print("Your current gold balance is: ",values[5],"\n")
    print("################################################\n")

#every single piece of information; gold; multipliers; streaks
def fullView():
    print("\n\n\n")
    print("################################################\n")
    print("Your current gold balance is: ",values[5],"\n")
    print("################################################\n")
    print("You've completed", values[0],"hard tasks\n")
    print("You've completed", values[1],"medium tasks\n")
    print("You've completed", values[2],"easy tasks\n")
    print("You've completed", values[3],"reminders\n")
    print("You've completed", values[4],"pomodoros\n")
    print("################################################\n")
    print("Your current maxMultiplier is", values[6],"\n")
    print("Your current remsMultiplier is", values[7],"\n")
    print("Your current pomsMultiplier is", values[8],"\n")
    print("Your current diffMultiplier is", values[9],"\n")
    print("Your current medMultiplier is", values[10],"\n")
    print("Your current easyMultiplier is", values[11],"\n")
    print("################################################\n\n")
    time.sleep(2)
    first()

first()
