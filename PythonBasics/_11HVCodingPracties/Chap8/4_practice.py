# # Question # 1 --> Greatest of the three numbers

# def greater(n1 , n2 , n3):
#     if n1>n2 and n1>n3:
#         return n1
#     if n2>n1 and n2>n3:
#         return n2
#     else:
#         return n3
    
# print("Greater Number is : ", greater(34,56,67))

# # Question # 2 --> Calsius to Fehrenheit
 
# def CtoF(tempinCel):
#     return (tempinCel * (9/5)) + 32

# print("The Fehrenheit of celius Temperture is : ", CtoF(0))
# print("The Fehrenheit of celius Temperture is : ", CtoF(23))

# # Question # 3 --> prevent a print() fucntion to end with new line
 
# print("Hello This is one print function:", end=" ")
# print("Hey This is new print and not end with new line Enjoy!") 

# # Question # 4 --> Recursion function to sum the n natural numbers

# def SumOfNatuarl(n):
#     if n==0:
#         return 0
#     else:
#         return n+SumOfNatuarl(n-1) 
    
# print("Sum of Natural Number of 10 is : ", SumOfNatuarl(10))

# # Question # 5 --> Function to print the line one less star after one

# def pattern(n):
#     for i in range(n,0,-1):
#          print("*" * i)

# pattern(4)

# # Question # 6 --> inches to cms

# def cms(inches):
#     return inches*2.54

# print("The cms of the inches 10 is: " , cms(10))
    
# Question # 7 --> Remove word form the list and strip it 

# strip() --> this fucntion remove white spaces from the list or string
# this ="   Hellow    "
# print(this.strip())


# def UpdateString(string,word):
#     nString = string.replace(word, "      ")
#     return nString.strip()
# print("Now the Update List is : " , UpdateString("      Hello World Tayyab    ","Hello"))

    
# Question # 8 -->  Function to print multiplication table of the given number

def table(n):
    for i in range(1,11):
        print(f"{n} * {i} = {n*i}")

table(6)