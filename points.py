import random
import json
import ast
import time


file = open("data.txt", "r+")
values = file.read().split(",")
maxMultiplier = float(values[6])
remsMultiplier = float(values[7])
pomsMultiplier = float(values[8])
diffMultiplier = float(values[9])
medMultiplier = float(values[10])
easyMultiplier = float(values[11])

def first():
    choice = input("Would you like to enter tasks {1} or go to spends {2} or would you like to just see values {3}?\nExit == 4\n")
    choice = int(choice)
    if(choice == 1 ):
        inputs()
        time.sleep(2)
        fullView()
    if(choice == 2):
        spend()
        time.sleep(2)
        gold()
    if(choice == 4):
        fullView()
        print("Thank you for using this service!")
    if(choice == 3):
        time.sleep(2)
        fullView()


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

def write(diff, med, easy, rems, poms, total):
    values.pop()
    values[0] = int(int(values[0])+diff)
    values[1] = int(int(values[1])+med)
    values[2] = int(int(values[2])+easy)
    values[3] = int(int(values[3])+rems)
    values[4] = int(int(values[4])+poms)
    values[5] = int(int(values[5])+total)
    values[7] = float(values[7])
    values[8] = float(values[8])
    values[9] = float(values[9])
    values[10] = float(values[10])
    values[11] = float(values[11])
    if(int(int(values[0])/5) != 0):
        value = float(values[0]/5)
        values[9] = round((values[9]* value /10)+ values[9],4)
    if(int(int(values[1])/5) != 0):
        value = float(values[1]/5)
        values[10] = round((values[10]* value /10)+ values[10],4)
    if(int(int(values[2])/5) != 0):
        value = float(values[2]/5)
        values[11] = round((values[11]* value /10)+ values[11],4)
    if(int(int(values[3])/5) != 0):
        value = float(values[3]/5)
        values[7] = round((values[7]* value /10)+ values[7],4)
    if(int(int(values[4])/5) != 0):
        value = float(values[4]/5)
        values[8] = round((values[8]* value /10)+ values[8],4)


    fullView()
    finalPrint()

def spend():
    spendFile = open("spends.txt","r")
    spends = spendFile.read()
    spends = ast.literal_eval(spends)
    response = input("Do you want to spend {1} or do you want to add new spends {2}?\n")
    if (int(response) == 1):
        for item in spends:
            print(item, "costs", spends[item])
        amount = input("How much are you spending?\n")
        amount = int(amount)
        prize = ""
        if(amount <= float(values[5])):
            values[5] -= amount;
            for key, value in spends.items():
                if amount == value:
                    prize = key
            print("You just bought: ", prize, "Enjoy!\n")
        else:
            print("Sorry, insufficient funds")
    if(int(response) == 2):
        spendFile = open("spends.txt","w")
        repeats = input("How many spends are you adding?\n")
        repeats = int(repeats)
        for x in range(repeats):
            name = input("What is the name?\n")
            cost = input("What is the cost?\n")
            cost = int(cost)
            spends[name]=cost
        spendFile.write(str(spends))
    finalPrint()

def finalPrint():
    file.close()
    fileNew = open("data.txt", "w")
    for value in values:
        fileNew.write(str(value)+",")
def gold():
    print("################################################\n")
    print("Your current gold balance is: ",values[5],"\n")
    print("################################################\n")
    
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
    print("\n\n\n")
    time.sleep(2)
    first()

first()
