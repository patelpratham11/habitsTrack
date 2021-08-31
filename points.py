import random

file = open("data.txt", "r+")
values = file.read().split(",")
maxMultiplier = float(values[6])
remsMultiplier = float(values[7])
pomsMultiplier = float(values[8])
diffMultiplier = float(values[9])
medMultiplier = float(values[10])
easyMultiplier = float(values[11])
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
        values[9] = (values[9]* value /0.1)+ values[9]
    if(int(int(values[1])/5) != 0):
        value = float(values[1]/5)
        values[10] = (values[10]* value /0.1)+ values[10]
    if(int(int(values[2])/5) != 0):
        value = float(values[2]/5)
        values[11] = (values[11]* value /0.1)+ values[11]
    if(int(int(values[3])/5) != 0):
        value = float(values[3]/5)
        values[7] = (values[7]* value /0.1)+ values[7]
    if(int(int(values[4])/5) != 0):
        value = float(values[4]/5)
        values[8] = (values[8]* value /0.1)+ values[8]


    print("You have earned: ", values[3], "gold\n")
    file.close()
    fileNew = open("data.txt", "w")
    for value in values:
        fileNew.write(str(value)+",")
inputs()
