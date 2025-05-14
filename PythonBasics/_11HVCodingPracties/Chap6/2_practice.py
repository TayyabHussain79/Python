# # Question 1 - Greator of the four number Enter by the User

# nm1=int(input("Enter No1: ")) 
# nm2=int(input("Enter No2: ")) 
# nm3=int(input("Enter No3: ")) 
# nm4=int(input("Enter No4: ")) 

# if(nm1>nm2 and nm1>nm3 and nm1>nm4):
#     print(nm1)
# elif(nm2>nm1 and nm2>nm3 and nm2>nm4):
#     print(nm2)
# elif(nm3>nm1 and nm3>nm2 and nm3>nm4):
#     print(nm3)
# else:
#     print(nm4)

# # Question 2 - Whether Student is pass or fail 

# ms1=int(input("Enter Marks of Subject 1: "))
# ms2=int(input("Enter Marks of Subject 2: "))
# ms3=int(input("Enter Marks of Subject 3: "))
# perc=(ms1+ms2+ms3)/3

# if(ms1<33 or ms2<33 or ms3<33):
#     print("Student is Fail Because of there mark in subject which is less than 33%")
# elif(perc<40):
#     print("Student is Fale Because of the total percentage which is ",perc)
# else:
#     print("Congrculation Student is Pass with percentage ",perc)


# # Question 3 - deteting spam words from the comment

# # comments="This is your lucky draw you can click here to get it.move forward make alot of money"
# comments=input("Enter the Text: To find it spam or not:\n ")

# if("click here" in comments or "subscribe this" in comments or "make alot of money" in comments):
#     print("This is Spam:") #or we can create elif conditon for each word
# else:
#     print("This Comment is out of Spam:")


# # Question 4 - Name contain length 10 or less
# name=input("Enter Your Name: ")
# if(len(name)<10):
#     print("Your Name " + name +" Length is less than 10")
# elif(len(name) == 10):
#     print("Name length is 10")
# else:
#     print("Name Length is greater than 10")


# # Question 5 - Name is present in list or not

# nameList=["Tayyab","Usama","Ahsan","Uzair","Adnan"]
# nme=input("Enter Your Name: ")
# if(nme in nameList): #its also work as if nme in nameList:
#     print(f"{nme} is in the List.")
# else:
#     print(f"{nme} is not in the List.")

# # Question 6 - Find grade of the Student
# print("******* Grade Program ********")
# msk1=int(input("Enter Marks of Subject 1: "))
# msk2=int(input("Enter Marks of Subject 2: "))
# msk3=int(input("Enter Marks of Subject 3: "))
# msk4=int(input("Enter Marks of Subject 4: "))
# msk5=int(input("Enter Marks of Subject 5: "))

# percentage=(msk1+msk2+msk3+msk4+msk5)/5

# # if(percentage<=100 and percentage>=90):
# #     print("Grade is Excellent")
# # elif(percentage<90 and percentage>=80):
# #     print("Grade is A")
# # elif(percentage<80 and percentage>=70):
# #     print("Grade is B")
# # elif(percentage<70 and percentage>=60):
# #     print("Grade is C")
# # elif(percentage<60 and percentage>=50):
# #     print("Grade is D")
# # elif(percentage<50 and percentage>=40):
# #     print("Grade is E")
# # else:
# #     print("Fail")

#     # Another way but as you wish
# if(percentage>=90):
#     print("Grade is Excellent")
# elif(percentage>=80):
#     print("Grade is A")
# elif(percentage>=70):
#     print("Grade is B")
# elif(percentage>=60):
#     print("Grade is C")
# elif(percentage>=50):
#     print("Grade is D")
# elif(percentage>=40):
#     print("Grade is E")
# else:
#     print("Fail")

# Quesiton 7 - Is this post is about Tayyab or not

post =input("Enter Post:\n")

if("Tayyab" in post):
    print("Yes This post is about Tayyab")
elif "tayyab" in post:
    print("Yes This post is about Tayyab")
elif "tAyyab" in post:
    print("Yes This post is about Tayyab")
elif "taYYab" in post:
    print("Yes This post is about Tayyab")
elif "tayYab" in post:
    print("Yes This post is about Tayyab")
elif "taYyab" in post:
    print("Yes This post is about Tayyab")
elif "tayyAb" in post:
    print("Yes This post is about Tayyab")
elif "tayyaB" in post:
    print("Yes This post is about Tayyab")
elif "TAyyab" in post:
    print("Yes This post is about Tayyab")
elif "tayyAB" in post:
    print("Yes This post is about Tayyab")
elif "tayYAB" in post:
    print("Yes This post is about Tayyab")
elif "TAYyab" in post:
    print("Yes This post is about Tayyab")
elif "TAYYab" in post:
    print("Yes This post is about Tayyab")
elif "TAYYAB" in post:
    print("Yes This post is about Tayyab")
elif "TAYYAb" in post:
    print("Yes This post is about Tayyab")
else:
    print("This post is not talking about Tayyab")
