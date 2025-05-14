# Question : 1 Create file and find it contain twinkle or not

# with open('poem.txt', 'w') as f:
#     f.write(" poem is here twinkle twinkel litter star How what so what so high like the diamend")

# with open('poem.txt', 'r') as f:
#     content = f.read()

# a = content.find("twinkle")
# print(a)

# Another Way to doing this is 

# with open('poem.txt', 'w') as f:
#     f.write(" poem is here twinkle twinkel litter star How what so what so high like the diamend")

# with open('poem.txt', 'r') as f:
#     content = f.read()

# if "twinkle" in content:
#     print("Yes it have")
# else:
#     print("It does not have")


# Question : 2 Game return high scroe

# def game():
#     return 100

# score= game()
# with open('History.txt' , 'r') as f:
#     HighScore= f.read()
#     if HighScore == '':
#         with open('History.txt' , 'w') as f:
#             f.write(str(score))
#     else:
#         HighScore = int(HighScore)
#         if score > HighScore:
#             with open('History.txt' , 'w') as f:
#                f.write(str(score))

# # checking
# with open('History.txt') as f:
#     scoreinUp = f.read()
# print(scoreinUp)
              


# Question 3 Multiplication table from 2 to 20 and store in different in the folder
 
# def Table(n):
#     with open(f"Tables/Table{n}.txt", 'w') as f:
#             for i in range(1,11):
#                f.write(f"{n} X {i} = {n*i} \n")

# for i in range(2 , 21):
#      Table(i)
    
# Question 4 : Replace word donkey from the file with ######
 
# with open('Donkey.txt', 'w') as f:
#     f.write("Donkey is the Donkey and monkey is also the Donkey")
# with open('Donkey.txt', 'r') as f:
#     content = f.read()

# UpdateContent= content.replace("Donkey","######")
    
# with open('Donkey.txt', 'w') as f:
#     f.write(UpdateContent)

# ------------------------------------------
# Replacing in list

# list=['Apple','Donkey','Mango','Donkey2','Donkey']

# for i in range(len(list)):
#     if list[i] == 'Donkey':
#         list[i]='######'

# print(list)
# -----------------------------------------

# Question : 5  doing above work if list of word in given to done the work above

list=['Apple','Donkey','monkey']
with open('Donkey.txt', 'w') as f:
    f.write("Donkey is the Donkey and monkey is also the Donkey")


# for i in range(len(list)):
#     with open('Donkey.txt', 'r') as f:
#       content = f.read()
#     UpdateContent= content.replace(list[i],"######")
#     with open('Donkey.txt', 'w') as f:
#        f.write(UpdateContent)

# # Another way of doing above just methed change
# with open('Donkey.txt', 'r') as f:
#       content = f.read()

# for word in list:
#     content= content.replace(word,"######")
#     with open('Donkey.txt', 'w') as f:
#        f.write(content)

# # Question 6: mine the log file and whether it contain word python or not even it captial sytax

# with open('log.txt') as f:
#     content = f.read()

# if 'python' in content.lower():
#     print("Yes python is present")
# else:
#     print("python is not present")

# Question 7 : Find the line number where word python is present in log file


# with open('log.txt') as f:
#     for i in range(1,30):
#         content = f.readline()
#         if 'python' in content.lower():
#             print(content)
#             print(f"Python is present at line: {i}")
#             break
        

# Another way --> Above method doesnot show only one line not multiple time

# content = True
# i=0
# with open('log.txt') as f:
#     while content:
#         i+=1
#         content = f.readline()
#         if 'python' in content.lower():
#             print(content)
#             print(f"Python is present at line: {i}")
        
# Question 8: That the file are identical or not
with open("swipe.txt") as f:
    file1 = f.read()
with open("swipe3.txt") as f:
    file2 = f.read()

if file1 == file2:
    print("Files are Same")
else:
    print("File are not Same")

# Question 9: Swipe content of the file (delete content of the file)
 
# with open('Swipe.txt', 'w') as f:
#     f.write("")

# Question 10: Rename the file 

# import os
# with open('Swipe2.txt') as f:
#     txt = f.read()
# with open('swipe.txt', 'w') as f:
#     f.write(txt)
# os.remove('Swipe2.txt')