# File in Python --> file can be read write and append in the python using funciton
# File must be closed after when you open it

# Read mode -- by defualt it is read mode
myFile = open('simple.txt', "r")
f = myFile.read()
# f = myFile.read(2)  # read only the first 2 character
# f = myFile.readline()  # readline is to read a single line the file

print(f)
myFile.close()

# Write Mode if file is not present it will create it
# (this is mode after close and write the previous content will remove)
myFile = open('simple.txt', 'w')
myFile.write("Hello this is a Write mode")
myFile.write("You can write multiple in the file the content will not remove but before closing it")
myFile.close()

# Append Mode by this the file can be open and you can append text add the end of the file
myFile = open('simple.txt', 'a')
myFile.write("Hello this is a append mode here at the end the text is added")
myFile.close()



# For binary file 
# mode is wb , wt(default text t)