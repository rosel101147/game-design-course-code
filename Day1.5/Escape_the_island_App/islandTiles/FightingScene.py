import random

HP_C = random.randint(2,6)
HP = 5
print("You encounter a wild crocodile. What will you do? ")

while battle == 1:
    print("The crocdile has " + HP_C + "HP. ")
    print("You have " + HP + "HP. ")
       
    print("Select a move:")
    Move = str(input(print("[A] Attack \n[B] Scare\n[C] Run Away")))
    if Move == 'A':
        Hit = random.randint(1, 3)
        if Hit == 4 or Hit == 3 or Hit == 2:
            damageRand = random.randint(1, 3)
            HP_C = HP_C - damageRand
            print("Success! Crocdile's HP is now " + HP_C + ".")
        else:
            print("Failure, no damage dealt.")
    elif Move == 'B':
        if(HP_C > HP):
            print("Failure, the crocodile is unafraid of you.")
            damageRand = random.randint(2, 3)
            HP = HP - damageRand
            print("The crocodilte attacked! You lost " + damageRand + "HP! ")
        else:
            scare = random.randint(1,3)
            if scare == 1:
                print("The crocodile ran away! The battle is now over.")
                battle = 0
    elif Move == "C":
        run = random.randint(1,5)
        if run == 5:
            print("You have run away! The battle is now over.")
        else:
            print("Your attempt at fleeing as unsuccessful!")
            damageRand = random.randint(2, 3)
            HP = HP - damageRand
            print("The crocodilte attacked! You lost " + damageRand + "HP! ")

    if HP_C < 1:
        print ("Congratulations! You killed the crocodile!")
        battle = 0
       
    elif HP < 1:
        print ("Oh no! You were killed by the crocodile!")
        print ("You have died. ")
        battle = 0