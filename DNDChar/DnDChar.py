#!python3
from random import randint
from StrengthMod import StrengthModi
from IntelMod import IntelModi


"""
The generator should do the following:
    Roll basic stats
    Choose a random race and class (if you can choose a class/race that best suits the stats, even better!)
    Apply race bonuses/penalties (bottom of p14)
    Show any bonuses from the basic stats (p9 Table2, p10 Table II, p11 Wisdom Table I and Dexterity Table I, p12 Constitution Table
    Choose a random level that is more weighted to pick a low level (1-5) than a high level
    Determine HP based on the tables for the individual classes p20-31
    Display the results in a format that is easily readable


    stat print in case i need it
    print(f"Strength: {StatList[0]}")
    print(f"Intelligence: {StatList[1]}")
    print(f"Wisdom: {StatList[2]}")
    print(f"Dexterity: {StatList[3]}")
    print(f"Constitution: {StatList[4]}")
    print(f"Charisma: {StatList[5]}")
"""
StatList = ["Strength", "Intelligence", "Wisdom", "Dexterity", "Constitution", "Charisma"]
Race = ""
Class = ""

def Stats():
    for i in range(6):
        dice1 = randint(1,6)
        dice2 = randint(1,6)
        dice3 = randint(1,6)
        roll = dice1 + dice2 + dice3
        StatList.pop(i)
        StatList.insert(i,roll)
    print(StatList)

def ClassRace():
    RaceList = ["Dwarf", "Elf", "Gnome", "Half-Elf", "Halfling", "Half-Orc", "Human"]
    ClassList = ["Druid", "Paladin", "Ranger", "Illusionist", "Assassin", "Monk"]
    RacePick = randint(0,6)
    ClassPick = randint(0,5)
    Race = RaceList[RacePick]
    Class = ClassList[ClassPick]
    if Race == "Dwarf":
        StatList[4] = StatList[4] + 1
        StatList[5] = StatList[5] - 1
    elif Race == "Elf":
        StatList[3] = StatList[3] + 1
        StatList[4] = StatList[4] - 1
    elif Race == "Half-Orc":
        StatList[0] = StatList[0] + 1
        StatList[4] = StatList[4] + 1
        StatList[5] = StatList[5] - 2
    elif Race == "Halfling":
        StatList[3] = StatList[3] + 1
        StatList[0] = StatList[0] - 1
    print(Race)
    print(Class)
    """
    [13,12,11,10,17,18]
    [0,0,0,1,-1,-2]
    for i in range(6):
        statList[i] = statList[i] + modifier[i]
    """



Stats()
print(StatList)
ClassRace()

StrengthModi(StatList)
IntelModi(StatList)
