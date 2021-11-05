from random import randint

"""
 Show any bonuses from the basic stats (p9 Table2, p10 Table II, p11 Wisdom Table I and Dexterity Table I, p12 Constitution Table
"""
StatList = ["Strength", "Intelligence", "Wisdom", "Dexterity", "Constitution", "Charisma"]

def Stats():
    for i in range(6):
        dice1 = randint(1,6)
        dice2 = randint(1,6)
        dice3 = randint(1,6)
        roll = dice1 + dice2 + dice3
        StatList.pop(i)
        StatList.insert(i,roll)
    print(StatList)


def StrengthModi(SList):
    if SList[0] == 3:
        print("Hit Probability:     -3")
        print("Damage Adjustment:   -1")
        print("Weight Allowance:   -350")
        print("Open Doors On A:      1")
        print("Bend Bars/Lift Gates: 0%")
    
    elif SList[0] == 4 or SList[0] == 5:
        print("Hit Probability:     -2")
        print("Damage Adjustment:   -1")
        print("Weight Allowance:   -250")
        print("Open Doors On A:      1")
        print("Bend Bars/Lift Gates: 0%")
    
    elif SList[0] == 6 or SList[0] == 7:
        print("Hit Probability:     -1")
        print("Damage Adjustment:   None")
        print("Weight Allowance:   -150")
        print("Open Doors On A:      1")
        print("Bend Bars/Lift Gates: 0%")
    
    elif SList[0] == 8 or SList[0] == 9:
        print("Hit Probability:      Normal")
        print("Damage Adjustment:    None")
        print("Weight Allowance:     Normal")
        print("Open Doors On A:      1-2")
        print("Bend Bars/Lift Gates: 1%")
    
    elif SList[0] == 10 or SList[0] == 11:
        print("Hit Probability:      Normal")
        print("Damage Adjustment:    None")
        print("Weight Allowance:     Normal")
        print("Open Doors On A:      1-2")
        print("Bend Bars/Lift Gates: 2%")
    
    elif SList[0] == 12 or SList[0] == 13:
        print("Hit Probability:      Normal")
        print("Damage Adjustment:    None")
        print("Weight Allowance:     +100")
        print("Open Doors On A:      1-2")
        print("Bend Bars/Lift Gates: 4%")
    
    elif SList[0] == 14 or SList[0] == 15:
        print("Hit Probability:      Normal")
        print("Damage Adjustment:    None")
        print("Weight Allowance:     +200")
        print("Open Doors On A:      1-2")
        print("Bend Bars/Lift Gates: 7%")
    
    elif SList[0] == 16:
        print("Hit Probability:      Normal")
        print("Damage Adjustment:    +1")
        print("Weight Allowance:     +350")
        print("Open Doors On A:      1-3")
        print("Bend Bars/Lift Gates: 10%")
    
    elif SList[0] == 17:
        print("Hit Probability:      +1")
        print("Damage Adjustment:    +1")
        print("Weight Allowance:     +500")
        print("Open Doors On A:      1-3")
        print("Bend Bars/Lift Gates: 13%")
    
    elif SList[0] == 18:
        print("Hit Probability:      +1")
        print("Damage Adjustment:    +2")
        print("Weight Allowance:     +750")
        print("Open Doors On A:      1-3")
        print("Bend Bars/Lift Gates: 16%")

