# input Function we use to take input from user in a string (even it is a nmber it take it as a string)
name=input("Enter a Name: ")
print(name)
print(type(name))


age = input("Enter your age: ")
print(age)
print(type(age)) # here age type is also string as it is number so we you type coversion

age=int(age)
print(type(age))