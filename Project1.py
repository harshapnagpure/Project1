import random
# snake , water , gun or rock paper scissors
def gameWin(comp, you):
    if comp == you:
        return None
    
    # check for all possibilities when computer chose s
    elif comp == 's':
         # if two values are equal, declare a tie !
        if you == "w":
            return False
        elif you =='g':
            return True
     # check for all possibilities when computer chose w
    elif comp == 'w':
        if you =='g':
            return False
        elif you=='s':
            return True
     # check for all possibilities when computer chose g
    elif comp == 'g':
        if you =='s':
            return False
        elif you=='w':
            return True
print("Comp Turn: Snake(s) water(w) or gun(g) ?")
randNo = random.randint(1, 3)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'

you =  input("Your's Turn: Snake(s) water(w) or gun(g) ?")
a = gameWin(comp, you)

print("Computer chose {comp}")
print(f"You chose {you}")
if a == None:
    print("The game is tie!")
elif a:
    print("You Win!!")
else:
    print("Lose!!")