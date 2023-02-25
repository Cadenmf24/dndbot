import numpy as np

initiative_list = []

# Code: Creates a list of enemies
# Code: Calculates Traps 
# Code: *Calculate Vermin Chance
def getinitiativeRoll(list):
        return list[1]
    

def addToList(player, number):
    
    player_turn = [player, number]
    
    initiative_list.append(player_turn)
    
    initiative_list.sort(reverse = True, key=getinitiativeRoll)
    
def rolltoLand(modifier):
    
    roll = np.randint(20)
    
    print("Rolled a " + roll + " With a " + modifier + "Resulting in a " + (roll+modifier))
    

def rollToDamage(dice, modifier):
    
    roll = np.randint(dice)
    
    print("Rolled a " + roll + " With a " + modifier + "Resulting in a " + (roll+modifier))
    
def main():
    
    print("Test")
    
main()