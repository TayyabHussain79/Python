def Greet(name):
    print("Best of Luck", name)


Greet("Tayyab")
Greet("Shani")
Greet("Ahsan")

# Default Parameter value:
# if user doesnot pass the argument then default value will show to the user

def Greet(name="Stranger"):
    print("Best of Luck", name)


Greet("Tayyab")
Greet("Shani")
Greet()


