# # Question 1 --> print multiplication table of the given number

# print("***** Table Program *****")
# num=int(input("Enter the Number: "))

# for i in range(1,11):
#     # print(str(num) + " * "+str(i)+" = "+str(num*i)) 
#     print(f"{num} * {i} = {num*i}")


# # Question 2 -- greet names in the list start with S 

# l1=["Tayyab","Usman","Tajaml","Ahsan"]

# for item in l1:
#     if item.startswith("T"):
#         print("Hello !", item)


# # Question 3 --Do program 1 with while loop

# print("***** Table Program *****")
# num=int(input("Enter the Number: "))
# i=1
# while i<=10: 
#     print(str(num) + " * "+str(i)+" = "+str(num*i))
#     i=i+1


# Question 4 -- Give number prime or not


# by while loop
# while True:
#     print("**** Prime Number Checking ****")
#     nm=int(input("Enter Number: "))
#     for i in range(2,nm):
#         if nm%i==0:     
#            print("Number is NOT Prime")
#            break
#     else:
#        print("Number is Prime")


# #------------------Answer 4 question
# print("**** Prime Number Checking ****")
# nm=int(input("Enter Number: "))

# for i in range(2,nm):
#     if nm%i == 0:
#         print(f"{nm} is not Prime")
#         break
# else:
#     print(f"{nm} is Prime")


# # Question 5 --> add first n natural number using while

# i=1
# Sum=0
# while i<100:
#     Sum=Sum+i
#     print("Sum is", Sum)
#     i=i+1


# # Question 6 -- Factorial of the number

print("**** Factorial Program ****")
nbr=int(input("Enter a Number: "))

# # # Through while
# fac=1
# while nbr!=0:
#     fac=fac*nbr
#     nbr=nbr-1
# else:
#     print(f"Factorial is {fac}")

# # Through for
fac=1
# for i in range(1,(nbr+1)):  # in acending order like 1*2*3 
for i in range(nbr,0,-1):       # oppsite to above
    fac=fac*i
    # nbr=nbr-1
else:
    print(f"Factorial of {nbr} is {fac}")


# Question 7 --> print * pattern

# for i in range(5):
#     print("*"*(i+1))


# # Queston 8 --> Also print pattern of *

# n=6
# for i in range(6):
#     print(" "*(n-1-i),end="")
#     print("*"*(2*i+1),end="")
#     print(" "*(n-1-i))

# # # Queston 9 --> Also print pattern of *

# n=10
# for i in range(n):
#     if i==0 or i==(n-1):
#         print("*"*n)
#     if i in range(1,(n-1)):
#         print("*"+" "*(n-2)+"*",)


# # Question 10 --> print multiplication table of the given number in reverse order

# print("***** Table Program *****")
# num=int(input("Enter the Number: "))

# for i in range(10,0,-1):
#     # print(str(num) + " * "+str(i)+" = "+str(num*i)) 
#     print(f"{num} * {i} = {num*i}")

# ــــــــــــــــ Another way to doing above 10 question is 

# print("***** Table Program REVERSE *****")
# num=int(input("Enter the Number: "))
# listTable=[]
# for i in range(1,11):
#     # print(str(num) + " * "+str(i)+" = "+str(num*i)) 
#     listTable.append(f"{num} * {i} = {num*i}")
# listTable.reverse()
# for i in range(len(listTable)):
#     print(listTable[i])

