# Practice of the Chapter 5

# Question 1 - create dictionary of urdu to English translation words

DicUToE ={
    "Wada": "Promise",
    "Alan": "Proclaim",
    "chalna":"Walk",
    "Khana":"Eat"
}
print("Options to select the Words:\n", list(DicUToE.keys()))
wrd=input("Enter Urdu Words to Translate In English:\n")
# print("Meaning is ",DicUToE[wrd]) #If words no present it show error
print("Meaning is ",DicUToE.get(wrd))

# Question 2 - Take eight number from user and display all the number unique

# n1=input("Enter First Number: ")
# n2=input("Enter 2 Number: ")
# n3=input("Enter 3 Number: ")
# n4=input("Enter 4 Number: ")
# n5=input("Enter 5 Number: ")
# n6=input("Enter 6 Number: ")
# n7=input("Enter 7 Number: ")
# n8=input("Enter 8 Number: ")
# n9=input("Enter 9 Number: ")

# numbers={n1,n2,n3,n4,n5,n6,n7,n8,n9}
# print(numbers)

# Question 3 - set with 18 value and "18" string

s1={18,"18"}
print(s1)


# Question 4 - Length of the following set
s=set()
print(len(s))

s.add(20)
s.add(20.0) #--> Here return 1 because 20.0 is same as 20
s.add(20.5) #--> Here return 2 because 20.5 is not same as 20
s.add("20")
print(len(s))


# Question 5 - Create Dictionary and allow four friend to add there favouite language as value and there keys are there name

dicL={}
# aL=input("Enter Language Ahsan: ")
# uL=input("Enter Language Uzair: ")
# usL=input("Enter Language Usamn: ")
# rL=input("Enter Language Rehan: ")

# dicL["ahsan"]=aL
# dicL["uzair"]=uL
# dicL["usman"]=usL
# dicL["rehan"]=rL

# print(dicL)

# Question 6 -