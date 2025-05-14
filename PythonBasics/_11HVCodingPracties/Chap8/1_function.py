# function --> Group of Statements perfrom specific task (can repeat any numb of time)
# Syntax


def Percent(marks):  #Fucntion Definition
    per= (sum(marks)/700)*100
    return per
    

maS1=[56,89,79,90,89,78,90]
maS2=[96,89,96,90,89,84,90]

# function Call

percentageStudent1 = Percent(maS1)
percentageStudent2 = Percent(maS2)

print("Percentage of Student One is", percentageStudent1)
print("Percentage of Student Two is", percentageStudent2)