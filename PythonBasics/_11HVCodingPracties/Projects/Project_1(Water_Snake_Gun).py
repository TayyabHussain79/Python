# ---------- Snake , Water , Gun Game ---------------------

# Import Random laberay to generate a random number for Computer Time
import random

# GameDecision Function Definition
def gameDecision(CompValue, UserValue):

    # If computer and user value is same then it tie means miss
    if CompValue == UserValue:
        return None
    
    # If Computer value is selected "s"
    elif CompValue == "s":
        if UserValue == "g":
            return True
        elif UserValue == "w":
            return False
    # If Computer value is selected "g"
    elif CompValue == "g":
        if UserValue == "w":
            return True
        elif UserValue == "s":
            return False
    # If Computer value is selected "w"
    elif CompValue == "w":
        if UserValue == "s":
            return True
        elif UserValue == "g":
            return False


# Computer Value
print("Computer Time: Select Snake(s) , Water(w) or Gun(g):")

# Random Number Selected From the randint
randomNumber = random.randint(1,3)
if randomNumber == 1:
    CompValue = "s"
elif randomNumber == 2:
    CompValue = "w"
elif randomNumber == 3:
    CompValue = "g"

# User Value
UserValue=input("Your's Time: Select Snake(s) , Water(w) or Gun(g):")

# Print Value that is selected by Computer and the User
print(f"Computer value is  {CompValue}")
print(f"Your value is  {UserValue}")

# Game Decision Funciton Call
Decision = gameDecision(CompValue,UserValue)

# If Decision is None
if Decision == None:
    print("Tie(Miss). Try Again!")
# If Decision is True 
elif Decision:
    print("You Win!")
# If Decision is False
else:
    print("You Lose!")