# String Function
introduction="hello Tayyab\\s how are you \n Are you good in programming"

# 1) len function

print(len(introduction))
print(len("Tayyab"))

# 2) endswith and startswith function

print(introduction.endswith("you"))
print(introduction.endswith("ing"))
print(introduction.startswith("Hello"))

# 3) count function

print(introduction.count("g"))
print(introduction.count("you"))

# 4) capitalize function

print(introduction.capitalize()) #--> its work 
            #  OR
cap= introduction.capitalize()
print(cap)

# 5) find funciton (index of first occurnes)
print(introduction.find("Tayyab"))
print(introduction.find("you"))

# 6) replace function (replace all occurness)

repintro= introduction.replace("Tayyab\\s", "Tayyab")
print(repintro)


# Escape Sequence characters
# like \n --> for few line in String
# like \t --> for tab in String
# like \' --> for ' in String
# like \\' --> for \ in String



