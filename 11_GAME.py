# GAME (Stone , Paper , Scissor)
import random

def game(comp, you):
    if comp == you:
        return None
    elif comp == 'Stone':
        if you == 'Scissor':
            return False
        elif you == '2':
            return True
    elif comp == 'Paper':
        if you == '1':
            return False
        elif you == '3':
            return True
    elif comp == 'Scissor':
        if you == '2':
            return False
        elif you == '1':
            return True

print("GAME START !!!")

randNO = random.randint(1, 3)
if randNO == 1:
    comp = 'Stone'
elif randNO == 2:
    comp = 'Paper'
elif randNO == 3:
    comp = 'Scissor'

you = int(input("Your Turn : Stone(1) , Paper(2) , Scissor(3) ? : "))
g = game(comp, you)
if you == 1:
    print("You chose : Stone")
elif you == 2:
    print("You chose : Paper")
elif you == 3:
    print("You chose : Scissor")
else:
    print("Wrong Input...")
#g = game(comp, you)
print(f"Computer chose:{comp}")
print(f"You chose:{you}")

if g == None:
    print("The game is a tie!")
elif g:
    print("You Win !")
else:
    print("You Lose  !")
