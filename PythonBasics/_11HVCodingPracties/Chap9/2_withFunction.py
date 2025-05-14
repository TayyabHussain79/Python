# This function is not require to closed the file

with open('simple.txt' , 'r') as f:
    filetext =f.read()
print(filetext)