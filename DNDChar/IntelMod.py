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


def IntelModi(IList):
    if IList[1] == 9:
        print("Chance to Know Each Listed Spell:    35%")
        print("Minimun Number of Spells/Level:      4")
        print("Maximum Number of Spells/Level:      6")
    
    elif IList[1] == 10 or IList[1] == 11 or IList[1] == 12:
        print("Chance to Know Each Listed Spell:    45%")
        print("Minimun Number of Spells/Level:      5")
        print("Maximum Number of Spells/Level:      7")
    
    elif IList[1] == 13 or IList[1] == 14:
        print("Chance to Know Each Listed Spell:    55%")
        print("Minimun Number of Spells/Level:      6")
        print("Maximum Number of Spells/Level:      9")
    
    elif IList[1] == 15 or IList[1] == 16:
        print("Chance to Know Each Listed Spell:    65%")
        print("Minimun Number of Spells/Level:      7")
        print("Maximum Number of Spells/Level:      11")
    
    elif IList[1] == 17:
        print("Chance to Know Each Listed Spell:    75%")
        print("Minimun Number of Spells/Level:      8")
        print("Maximum Number of Spells/Level:      14")
    
    elif IList[1] == 18:
        print("Chance to Know Each Listed Spell:    85%")
        print("Minimun Number of Spells/Level:      9")
        print("Maximum Number of Spells/Level:      18")
    

    

